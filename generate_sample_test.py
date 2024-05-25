import json
from datetime import datetime
from app import create_app, db  # Ensure your create_app function is properly defined in app.py
from models import Question

# Initialize the Flask app context
app = create_app()
app.app_context().push()

def generate_test(rubric_config_path):
    try:
        with open(rubric_config_path, 'r') as file:
            config = json.load(file)
    except FileNotFoundError:
        print(f"Error: The file '{rubric_config_path}' was not found.")
        return
    except json.JSONDecodeError:
        print(f"Error: The file '{rubric_config_path}' is not a valid JSON file.")
        return
    
    exam = config['exam']
    total_questions = exam['total_questions']
    sections = exam['sections']
    
    generated_test = {
        "title": exam['title'],
        "time_limit": exam['time_limit_minutes'],
        "sections": []
    }

    for section in sections:
        section_name = section['name']
        questions_list = []

        for question_group in section['questions']:
            question_type = question_group['type']
            count = question_group['count']
            difficulty_distribution = question_group['difficulty_distribution']
            topic_distribution = question_group['topic_distribution']

            questions = fetch_questions_from_db(
                question_type, count, difficulty_distribution, topic_distribution
            )
            questions_list.extend(questions)
            print(f"Fetched {len(questions)} questions for section {section_name}, question type {question_type}")

        generated_test["sections"].append({
            "name": section_name,
            "questions": [q.to_dict() for q in questions_list]
        })

    return generated_test

def fetch_questions_from_db(question_type, count, difficulty_distribution, topic_distribution):
    questions = []
    total_distribution = sum(difficulty_distribution.values())
    
    for difficulty, percentage in difficulty_distribution.items():
        difficulty_count = int((percentage / total_distribution) * count)
        print(f"Fetching {difficulty_count} questions of difficulty '{difficulty}'")

        for topic, topic_count in topic_distribution.items():
            print(f"Fetching questions for topic '{topic}', type '{question_type}', difficulty '{difficulty}'")
            topic_questions = Question.query.filter_by(
                question_type=question_type,
                difficulty=difficulty,
                topic=topic
            ).limit(difficulty_count).all()

            print(f"Found {len(topic_questions)} questions for topic '{topic}', type '{question_type}', difficulty '{difficulty}'")
            questions.extend(topic_questions)
    
    return questions

def main():
    rubric_config_path = './rubric_config.json'
    test = generate_test(rubric_config_path)
    if test:
        print(json.dumps(test, indent=4))
    else:
        print("Failed to generate test")

if __name__ == '__main__':
    main()
