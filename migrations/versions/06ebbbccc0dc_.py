"""empty message

Revision ID: 06ebbbccc0dc
Revises: e3b99fa74e63
Create Date: 2024-05-26 11:05:55.170360

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '06ebbbccc0dc'
down_revision = 'e3b99fa74e63'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('rubric', schema=None) as batch_op:
        batch_op.alter_column('sections',
               existing_type=sa.TEXT(),
               nullable=False)
        batch_op.drop_column('randomization')
        batch_op.drop_column('time_limit')
        batch_op.drop_column('difficulty_levels')
        batch_op.drop_column('question_types')
        batch_op.drop_column('coverage')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('rubric', schema=None) as batch_op:
        batch_op.add_column(sa.Column('coverage', sa.TEXT(), nullable=True))
        batch_op.add_column(sa.Column('question_types', sa.TEXT(), nullable=False))
        batch_op.add_column(sa.Column('difficulty_levels', sa.TEXT(), nullable=True))
        batch_op.add_column(sa.Column('time_limit', sa.INTEGER(), nullable=True))
        batch_op.add_column(sa.Column('randomization', sa.BOOLEAN(), nullable=True))
        batch_op.alter_column('sections',
               existing_type=sa.TEXT(),
               nullable=True)

    # ### end Alembic commands ###