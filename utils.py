from flask import request
from sqlalchemy import or_

def apply_filters(query, model, search_fields, filter_fields):
    search = request.args.get('search')
    if search:
        filters = [getattr(model, field).ilike(f'%{search}%') for field in search_fields]
        query = query.filter(or_(*filters))
    
    for field in filter_fields:
        value = request.args.get(field)
        if value:
            query = query.filter(getattr(model, field) == value)
    
    return query

def apply_sorting(query, model):
    sort_by = request.args.get('sort_by', 'id')  # Default to 'id' if not provided or empty
    if not sort_by or not hasattr(model, sort_by):
        sort_by = 'id'  # Ensure sort_by is valid and falls back to 'id'
    sort_order = request.args.get('sort_order', 'asc')
    if sort_order == 'asc':
        query = query.order_by(getattr(model, sort_by).asc())
    else:
        query = query.order_by(getattr(model, sort_by).desc())
    
    return query

def apply_pagination(query):
    per_page = int(request.args.get('per_page', 50))
    page = int(request.args.get('page', 1))
    pagination = query.paginate(page=page, per_page=per_page, error_out=False)
    return pagination.items, pagination.total, pagination
