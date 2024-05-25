import random
from app import app
from models import db, Course, CourseOutcome, Question


# Dummy data for courses
courses = [
    {"course_code": "CS103", "name": "Introduction to Programming", "school": "SOET", "department": "Computer Science", "outcomes": [
        {"number": 1, "description": "Understand the basic concepts of programming."},
        {"number": 2, "description": "Write simple programs using loops and conditionals."},
        {"number": 3, "description": "Debug and test code effectively."}
    ]},
    {"course_code": "MATH203", "name": "Linear Algebra", "school": "SMAS", "department": "Mathematics", "outcomes": [
        {"number": 1, "description": "Solve systems of linear equations."},
        {"number": 2, "description": "Understand vector spaces and subspaces."},
        {"number": 3, "description": "Apply linear transformations and matrices."}
    ]},
    {"course_code": "ENG303", "name": "Creative Writing", "school": "SOAS", "department": "English", "outcomes": [
        {"number": 1, "description": "Develop original creative writing pieces."},
        {"number": 2, "description": "Analyze and critique literary works."},
        {"number": 3, "description": "Enhance storytelling and narrative skills."}
    ]},
    {"course_code": "BIO204", "name": "Human Anatomy", "school": "SMAS", "department": "Biology", "outcomes": [
        {"number": 1, "description": "Identify and describe the major structures of the human body."},
        {"number": 2, "description": "Understand the functions of different body systems."},
        {"number": 3, "description": "Apply anatomical knowledge in practical contexts."}
    ]},
    {"course_code": "CHEM103", "name": "Analytical Chemistry", "school": "SMAS", "department": "Chemistry", "outcomes": [
        {"number": 1, "description": "Understand the principles of analytical techniques."},
        {"number": 2, "description": "Perform qualitative and quantitative analysis."},
        {"number": 3, "description": "Interpret experimental data accurately."}
    ]},
    {"course_code": "CS103", "name": "Introduction to Programming", "school": "SOET", "department": "Computer Science", "outcomes": [
        {"number": 1, "description": "Understand the basic concepts of programming."},
        {"number": 2, "description": "Write simple programs using loops and conditionals."},
        {"number": 3, "description": "Debug and test code effectively."}
    ]},
    {"course_code": "MATH203", "name": "Linear Algebra", "school": "SMAS", "department": "Mathematics", "outcomes": [
        {"number": 1, "description": "Solve systems of linear equations."},
        {"number": 2, "description": "Understand vector spaces and subspaces."},
        {"number": 3, "description": "Apply linear transformations and matrices."}
    ]},
    {"course_code": "ENG303", "name": "Creative Writing", "school": "SOAS", "department": "English", "outcomes": [
        {"number": 1, "description": "Develop original creative writing pieces."},
        {"number": 2, "description": "Analyze and critique literary works."},
        {"number": 3, "description": "Enhance storytelling and narrative skills."}
    ]},
    {"course_code": "BIO204", "name": "Human Anatomy", "school": "SMAS", "department": "Biology", "outcomes": [
        {"number": 1, "description": "Identify and describe the major structures of the human body."},
        {"number": 2, "description": "Understand the functions of different body systems."},
        {"number": 3, "description": "Apply anatomical knowledge in practical contexts."}
    ]},
    {"course_code": "CHEM103", "name": "Analytical Chemistry", "school": "SMAS", "department": "Chemistry", "outcomes": [
        {"number": 1, "description": "Understand the principles of analytical techniques."},
        {"number": 2, "description": "Perform qualitative and quantitative analysis."},
        {"number": 3, "description": "Interpret experimental data accurately."}
    ]},
    {"course_code": "CS104", "name": "Data Structures", "school": "SOET", "department": "Computer Science", "outcomes": [
        {"number": 1, "description": "Understand different types of data structures."},
        {"number": 2, "description": "Implement data structures in programming."},
        {"number": 3, "description": "Analyze the efficiency of algorithms using data structures."},
        {"number": 4, "description": "Apply data structures in real-world applications."}
    ]},
    {"course_code": "MATH204", "name": "Calculus II", "school": "SMAS", "department": "Mathematics", "outcomes": [
        {"number": 1, "description": "Understand advanced integration techniques."},
        {"number": 2, "description": "Apply calculus to solve real-world problems."},
        {"number": 3, "description": "Analyze series and sequences."},
        {"number": 4, "description": "Understand multivariable calculus."}
    ]},
    {"course_code": "ENG304", "name": "Advanced Literary Analysis", "school": "SOAS", "department": "English", "outcomes": [
        {"number": 1, "description": "Develop advanced skills in literary analysis."},
        {"number": 2, "description": "Critique and analyze complex texts."},
        {"number": 3, "description": "Apply literary theories to various works."},
        {"number": 4, "description": "Understand the historical context of literary movements."}
    ]},
    {"course_code": "BIO205", "name": "Genetics", "school": "SMAS", "department": "Biology", "outcomes": [
        {"number": 1, "description": "Understand the principles of inheritance."},
        {"number": 2, "description": "Analyze genetic patterns and mutations."},
        {"number": 3, "description": "Apply genetic knowledge in practical scenarios."},
        {"number": 4, "description": "Understand modern genetic technologies."},
        {"number": 5, "description": "Evaluate ethical considerations in genetics."}
    ]},
    {"course_code": "PHYS203", "name": "Electromagnetism", "school": "SMAS", "department": "Physics", "outcomes": [
        {"number": 1, "description": "Understand the principles of electromagnetism."},
        {"number": 2, "description": "Apply Maxwell's equations."},
        {"number": 3, "description": "Analyze electromagnetic waves."},
        {"number": 4, "description": "Understand the interaction between electric and magnetic fields."},
        {"number": 5, "description": "Apply electromagnetism in practical contexts."}
    ]},
    {"course_code": "CS205", "name": "Operating Systems", "school": "SOET", "department": "Computer Science", "outcomes": [
        {"number": 1, "description": "Understand the concepts of operating systems."},
        {"number": 2, "description": "Analyze process management and scheduling."},
        {"number": 3, "description": "Understand memory management."},
        {"number": 4, "description": "Apply knowledge of file systems."},
        {"number": 5, "description": "Understand concurrency and synchronization."},
        {"number": 6, "description": "Analyze case studies of different operating systems."}
    ]},
    {"course_code": "MATH305", "name": "Probability and Statistics", "school": "SMAS", "department": "Mathematics", "outcomes": [
        {"number": 1, "description": "Understand the basic concepts of probability."},
        {"number": 2, "description": "Apply probability distributions."},
        {"number": 3, "description": "Analyze statistical data."},
        {"number": 4, "description": "Apply statistical methods in real-world scenarios."},
        {"number": 5, "description": "Understand hypothesis testing."},
        {"number": 6, "description": "Evaluate statistical models."}
    ]},
    {"course_code": "ENG305", "name": "Shakespearean Literature", "school": "SOAS", "department": "English", "outcomes": [
        {"number": 1, "description": "Analyze the themes in Shakespeare's works."},
        {"number": 2, "description": "Understand the historical context of Shakespeare's time."},
        {"number": 3, "description": "Critique major plays and sonnets."},
        {"number": 4, "description": "Apply literary analysis to Shakespearean texts."},
        {"number": 5, "description": "Develop original interpretations of Shakespeare's works."},
        {"number": 6, "description": "Understand Shakespeare's influence on modern literature."}
    ]},
    {"course_code": "BIO306", "name": "Microbiology", "school": "SMAS", "department": "Biology", "outcomes": [
        {"number": 1, "description": "Understand the principles of microbiology."},
        {"number": 2, "description": "Analyze the structure and function of microorganisms."},
        {"number": 3, "description": "Apply microbiological techniques."},
        {"number": 4, "description": "Understand the role of microorganisms in disease."},
        {"number": 5, "description": "Evaluate the applications of microbiology in industry and research."},
        {"number": 6, "description": "Analyze case studies in microbiology."}
    ]},
    {"course_code": "CHEM205", "name": "Organic Chemistry", "school": "SMAS", "department": "Chemistry", "outcomes": [
        {"number": 1, "description": "Understand the principles of organic chemistry."},
        {"number": 2, "description": "Analyze the structure and reactivity of organic molecules."},
        {"number": 3, "description": "Apply organic chemistry in synthesis."},
        {"number": 4, "description": "Understand mechanisms of organic reactions."},
        {"number": 5, "description": "Evaluate the role of organic chemistry in pharmaceuticals."}
    ]},
    {"course_code": "CS206", "name": "Database Management Systems", "school": "SOET", "department": "Computer Science", "outcomes": [
        {"number": 1, "description": "Understand the concepts of database management."},
        {"number": 2, "description": "Design and implement relational databases."},
        {"number": 3, "description": "Analyze SQL queries."},
        {"number": 4, "description": "Apply database normalization techniques."},
        {"number": 5, "description": "Understand transaction management and concurrency control."},
        {"number": 6, "description": "Evaluate case studies of database systems."}
    ]},
    {"course_code": "MATH306", "name": "Discrete Mathematics", "school": "SMAS", "department": "Mathematics", "outcomes": [
        {"number": 1, "description": "Understand the principles of discrete mathematics."},
        {"number": 2, "description": "Analyze algorithms and their complexity."},
        {"number": 3, "description": "Apply graph theory."},
        {"number": 4, "description": "Understand combinatorics."},
        {"number": 5, "description": "Evaluate applications of discrete mathematics in computer science."},
        {"number": 6, "description": "Analyze case studies in discrete mathematics."}
    ]},
    {"course_code": "ENG306", "name": "Modern Poetry", "school": "SOAS", "department": "English", "outcomes": [
        {"number": 1, "description": "Analyze themes in modern poetry."},
        {"number": 2, "description": "Understand the historical context of modern poetry."},
        {"number": 3, "description": "Critique major works of modern poets."},
        {"number": 4, "description": "Apply literary analysis to modern poetry."},
        {"number": 5, "description": "Develop original interpretations of modern poems."},
        {"number": 6, "description": "Understand the influence of modern poetry on contemporary literature."},
        {"number": 7, "description": "Evaluate the role of modern poetry in social and political movements."}
    ]},
    {"course_code": "BIO307", "name": "Ecology", "school": "SMAS", "department": "Biology", "outcomes": [
        {"number": 1, "description": "Understand the principles of ecology."},
        {"number": 2, "description": "Analyze the interactions between organisms and their environments."},
        {"number": 3, "description": "Apply ecological concepts to conservation."},
        {"number": 4, "description": "Understand ecosystem dynamics."},
        {"number": 5, "description": "Evaluate the impact of human activities on ecosystems."},
        {"number": 6, "description": "Analyze case studies in ecology."}
    ]},
    {"course_code": "CHEM206", "name": "Physical Chemistry", "school": "SMAS", "department": "Chemistry", "outcomes": [
        {"number": 1, "description": "Understand the principles of physical chemistry."},
        {"number": 2, "description": "Analyze thermodynamic systems."},
        {"number": 3, "description": "Apply quantum chemistry."},
        {"number": 4, "description": "Understand chemical kinetics."},
        {"number": 5, "description": "Evaluate the role of physical chemistry in materials science."}
    ]},
    {"course_code": "CS207", "name": "Computer Networks", "school": "SOET", "department": "Computer Science", "outcomes": [
        {"number": 1, "description": "Understand the principles of computer networks."},
        {"number": 2, "description": "Analyze network protocols and architectures."},
        {"number": 3, "description": "Apply network security measures."},
        {"number": 4, "description": "Understand wireless and mobile networks."},
        {"number": 5, "description": "Evaluate case studies of computer networks."}
    ]},
    {"course_code": "MATH307", "name": "Differential Equations", "school": "SMAS", "department": "Mathematics", "outcomes": [
        {"number": 1, "description": "Understand the principles of differential equations."},
        {"number": 2, "description": "Solve ordinary differential equations."},
        {"number": 3, "description": "Apply differential equations to model real-world phenomena."},
        {"number": 4, "description": "Understand partial differential equations."},
        {"number": 5, "description": "Analyze the stability of solutions."}
    ]},
    {"course_code": "ENG307", "name": "World Literature", "school": "SOAS", "department": "English", "outcomes": [
        {"number": 1, "description": "Analyze themes in world literature."},
        {"number": 2, "description": "Understand the cultural and historical context of world literature."},
        {"number": 3, "description": "Critique major works from different cultures."},
        {"number": 4, "description": "Apply literary analysis to world literature."},
        {"number": 5, "description": "Develop original interpretations of world literary works."}
    ]},
    {"course_code": "BIO308", "name": "Biochemistry", "school": "SMAS", "department": "Biology", "outcomes": [
        {"number": 1, "description": "Understand the principles of biochemistry."},
        {"number": 2, "description": "Analyze the structure and function of biomolecules."},
        {"number": 3, "description": "Apply biochemical techniques."},
        {"number": 4, "description": "Understand metabolic pathways."},
        {"number": 5, "description": "Evaluate the role of biochemistry in health and disease."}
    ]},
    {"course_code": "CHEM103", "name": "Analytical Chemistry", "school": "SMAS", "department": "Chemistry", "outcomes": [
        {"number": 1, "description": "Understand the principles of analytical techniques."},
        {"number": 2, "description": "Perform qualitative and quantitative analysis."},
        {"number": 3, "description": "Interpret experimental data accurately."}
    ]}
]

# Dummy data for questions
questions = [
    {"content": "What is a variable in programming?", "course_id": 1, "bloom_level": "Remember", "topic": "Basics", "difficulty": "Easy", "question_type": "Single Correct Answer", "options": "A container for data,A function,A loop", "correct_answer": "A container for data"},
    {"content": "Solve the system of equations: 2x + 3y = 6, x - y = 4", "course_id": 2, "bloom_level": "Apply", "topic": "Systems of Equations", "difficulty": "Medium", "question_type": "Single Correct Answer", "options": "(2, 0),(0, 2),(1, 1)", "correct_answer": "(2, 0)"},
    {"content": "What is the main theme of '1984' by George Orwell?", "course_id": 3, "bloom_level": "Analyze", "topic": "Themes", "difficulty": "Medium", "question_type": "Single Correct Answer", "options": "Totalitarianism,Freedom,Love", "correct_answer": "Totalitarianism"},
    {"content": "Name the muscle responsible for pumping blood through the human body.", "course_id": 4, "bloom_level": "Remember", "topic": "Circulatory System", "difficulty": "Easy", "question_type": "Single Correct Answer", "options": "Heart,Liver,Kidney", "correct_answer": "Heart"},
    {"content": "Which technique is used for separation of components in a mixture?", "course_id": 5, "bloom_level": "Understand", "topic": "Separation Techniques", "difficulty": "Medium", "question_type": "Single Correct Answer", "options": "Chromatography,Distillation,Filtration", "correct_answer": "Chromatography"},
    {"content": "What is a variable in programming?", "course_id": 6, "bloom_level": "Remember", "topic": "Basics", "difficulty": "Easy", "question_type": "Single Correct Answer", "options": "A container for data,A function,A loop", "correct_answer": "A container for data"},
    {"content": "Solve the system of equations: 2x + 3y = 6, x - y = 4", "course_id": 7, "bloom_level": "Apply", "topic": "Systems of Equations", "difficulty": "Medium", "question_type": "Single Correct Answer", "options": "(2, 0),(0, 2),(1, 1)", "correct_answer": "(2, 0)"},
    {"content": "What is the main theme of '1984' by George Orwell?", "course_id": 8, "bloom_level": "Analyze", "topic": "Themes", "difficulty": "Medium", "question_type": "Single Correct Answer", "options": "Totalitarianism,Freedom,Love", "correct_answer": "Totalitarianism"},
    {"content": "Name the muscle responsible for pumping blood through the human body.", "course_id": 9, "bloom_level": "Remember", "topic": "Circulatory System", "difficulty": "Easy", "question_type": "Single Correct Answer", "options": "Heart,Liver,Kidney", "correct_answer": "Heart"},
    {"content": "Which technique is used for separation of components in a mixture?", "course_id": 10, "bloom_level": "Understand", "topic": "Separation Techniques", "difficulty": "Medium", "question_type": "Single Correct Answer", "options": "Chromatography,Distillation,Filtration", "correct_answer": "Chromatography"},
    {"content": "What is a pointer in C programming?", "course_id": 11, "bloom_level": "Remember", "topic": "Pointers", "difficulty": "Easy", "question_type": "Single Correct Answer", "options": "A variable that stores a memory address,A loop structure,A function", "correct_answer": "A variable that stores a memory address"},
    {"content": "Evaluate the integral of sin(x)dx from 0 to pi.", "course_id": 12, "bloom_level": "Apply", "topic": "Integration", "difficulty": "Medium", "question_type": "Single Correct Answer", "options": "2,1,0", "correct_answer": "2"},
    {"content": "Identify the main character in 'Hamlet'.", "course_id": 13, "bloom_level": "Remember", "topic": "Characters", "difficulty": "Easy", "question_type": "Single Correct Answer", "options": "Hamlet,Ophelia,Claudius", "correct_answer": "Hamlet"},
    {"content": "Which blood type is known as the universal donor?", "course_id": 14, "bloom_level": "Remember", "topic": "Blood Types", "difficulty": "Easy", "question_type": "Single Correct Answer", "options": "O negative,A positive,B negative", "correct_answer": "O negative"},
    {"content": "Determine the molecular weight of H2O.", "course_id": 15, "bloom_level": "Understand", "topic": "Molecular Weight", "difficulty": "Medium", "question_type": "Single Correct Answer", "options": "18 g/mol,20 g/mol,16 g/mol", "correct_answer": "18 g/mol"},
    {"content": "What is the time complexity of binary search?", "course_id": 16, "bloom_level": "Analyze", "topic": "Algorithms", "difficulty": "Medium", "question_type": "Single Correct Answer", "options": "O(log n),O(n),O(n^2)", "correct_answer": "O(log n)"},
    {"content": "Find the derivative of e^x.", "course_id": 17, "bloom_level": "Apply", "topic": "Derivatives", "difficulty": "Easy", "question_type": "Single Correct Answer", "options": "e^x,x e^x,e", "correct_answer": "e^x"},
    {"content": "What is the main conflict in 'Macbeth'?", "course_id": 18, "bloom_level": "Analyze", "topic": "Conflict", "difficulty": "Medium", "question_type": "Single Correct Answer", "options": "Ambition and power,Guilt and redemption,Love and betrayal", "correct_answer": "Ambition and power"},
    {"content": "Identify the process of photosynthesis.", "course_id": 19, "bloom_level": "Remember", "topic": "Photosynthesis", "difficulty": "Easy", "question_type": "Single Correct Answer", "options": "Conversion of light energy to chemical energy,Breakdown of glucose to release energy,Formation of proteins from amino acids", "correct_answer": "Conversion of light energy to chemical energy"},
    {"content": "Which law explains the relationship between pressure and volume of a gas?", "course_id": 20, "bloom_level": "Understand", "topic": "Gas Laws", "difficulty": "Medium", "question_type": "Single Correct Answer", "options": "Boyle's Law,Charles's Law,Avogadro's Law", "correct_answer": "Boyle's Law"},
    {"content": "Define the concept of inheritance in OOP.", "course_id": 21, "bloom_level": "Understand", "topic": "OOP Concepts", "difficulty": "Easy", "question_type": "Single Correct Answer", "options": "A mechanism to derive new classes from existing ones,A process of copying data,An algorithm to sort data", "correct_answer": "A mechanism to derive new classes from existing ones"},
    {"content": "Calculate the area under the curve y = x^2 from x = 0 to x = 2.", "course_id": 22, "bloom_level": "Apply", "topic": "Integration", "difficulty": "Medium", "question_type": "Single Correct Answer", "options": "8/3,4,2", "correct_answer": "8/3"},
    {"content": "Identify the protagonist in 'Pride and Prejudice'.", "course_id": 23, "bloom_level": "Remember", "topic": "Characters", "difficulty": "Easy", "question_type": "Single Correct Answer", "options": "Elizabeth Bennet,Mr. Darcy,Jane Bennet", "correct_answer": "Elizabeth Bennet"},
    {"content": "Describe the function of the mitochondria.", "course_id": 24, "bloom_level": "Understand", "topic": "Cell Biology", "difficulty": "Easy", "question_type": "Single Correct Answer", "options": "Production of energy,Protein synthesis,Photosynthesis", "correct_answer": "Production of energy"},
    {"content": "Which element is known as the 'king of chemicals'?", "course_id": 25, "bloom_level": "Remember", "topic": "Elements", "difficulty": "Medium", "question_type": "Single Correct Answer", "options": "Sulfuric acid,HCl,NaCl", "correct_answer": "Sulfuric acid"},
    {"content": "Differentiate between arrays and linked lists.", "course_id": 26, "bloom_level": "Analyze", "topic": "Data Structures", "difficulty": "Medium", "question_type": "Short Answer", "correct_answer": "Arrays have fixed size and continuous memory allocation, while linked lists have dynamic size and scattered memory allocation."},
    {"content": "Explain the concept of eigenvalues and eigenvectors.", "course_id": 27, "bloom_level": "Understand", "topic": "Linear Algebra", "difficulty": "Medium", "question_type": "Short Answer", "correct_answer": "Eigenvalues are scalars associated with a linear system of equations that, when multiplied by an eigenvector, do not change the direction of the eigenvector."},
    {"content": "Compare the themes of 'Pride and Prejudice' and 'Wuthering Heights'.", "course_id": 28, "bloom_level": "Analyze", "topic": "Themes", "difficulty": "Medium", "question_type": "Short Answer", "correct_answer": "While 'Pride and Prejudice' explores themes of social class and marriage, 'Wuthering Heights' focuses on revenge and the destructive nature of love."},
    {"content": "Describe the role of the pancreas in the human body.", "course_id": 29, "bloom_level": "Understand", "topic": "Digestive System", "difficulty": "Medium", "question_type": "Short Answer", "correct_answer": "The pancreas produces digestive enzymes and hormones such as insulin, which regulate blood sugar levels."},
    {"content": "Explain the process of esterification.", "course_id": 30, "bloom_level": "Understand", "topic": "Organic Chemistry", "difficulty": "Medium", "question_type": "Short Answer", "correct_answer": "Esterification is a chemical reaction between an acid and an alcohol, with the elimination of water, resulting in the formation of an ester."},
    {"content": "True or False: Inheritance allows for code reuse in OOP.", "course_id": 31, "bloom_level": "Understand", "topic": "OOP Concepts", "difficulty": "Easy", "question_type": "True/False", "correct_answer": "True"},
    {"content": "True or False: The limit of (sin x)/x as x approaches 0 is 1.", "course_id": 32, "bloom_level": "Apply", "topic": "Limits", "difficulty": "Easy", "question_type": "True/False", "correct_answer": "True"},
    {"content": "True or False: The main conflict in 'The Great Gatsby' is between wealth and poverty.", "course_id": 33, "bloom_level": "Analyze", "topic": "Conflict", "difficulty": "Medium", "question_type": "True/False", "correct_answer": "False"},
    {"content": "True or False: The heart is a part of the circulatory system.", "course_id": 34, "bloom_level": "Remember", "topic": "Circulatory System", "difficulty": "Easy", "question_type": "True/False", "correct_answer": "True"},
    {"content": "True or False: Boyle's Law relates pressure and temperature of a gas.", "course_id": 35, "bloom_level": "Understand", "topic": "Gas Laws", "difficulty": "Medium", "question_type": "True/False", "correct_answer": "False"},
    {"content": "Match the following data structures with their descriptions:", "course_id": 36, "bloom_level": "Understand", "topic": "Data Structures", "difficulty": "Medium", "question_type": "Matching", "pairs": "Array:Fixed size data structure,Linked List:Dynamic size data structure,Stack:LIFO data structure,Queue:FIFO data structure"},
    {"content": "Match the following calculus concepts with their definitions:", "course_id": 37, "bloom_level": "Understand", "topic": "Calculus", "difficulty": "Medium", "question_type": "Matching", "pairs": "Derivative:Rate of change,Integral:Area under the curve,Limit:Value approached by a function,Series:Sum of a sequence of terms"},
    {"content": "Match the following literary terms with their meanings:", "course_id": 38, "bloom_level": "Remember", "topic": "Literary Terms", "difficulty": "Easy", "question_type": "Matching", "pairs": "Metaphor:Comparison without 'like' or 'as',Simile:Comparison using 'like' or 'as',Personification:Giving human traits to non-human objects,Alliteration:Repetition of initial consonant sounds"},
    {"content": "Match the following body systems with their functions:", "course_id": 39, "bloom_level": "Remember", "topic": "Body Systems", "difficulty": "Easy", "question_type": "Matching", "pairs": "Circulatory:System that transports blood,Respiratory:System that facilitates breathing,Digestive:System that processes food,Nervous:System that transmits signals"},
    {"content": "Match the following chemical reactions with their descriptions:", "course_id": 40, "bloom_level": "Understand", "topic": "Chemical Reactions", "difficulty": "Medium", "question_type": "Matching", "pairs": "Combustion:Reaction with oxygen producing heat,Neutralization:Reaction between acid and base,Oxidation:Loss of electrons,Reduction:Gain of electrons"},
    {"content": "Fill in the blank: A data structure that follows LIFO is called a ______.", "course_id": 41, "bloom_level": "Understand", "topic": "Data Structures", "difficulty": "Easy", "question_type": "Fill in the Blank", "correct_answer": "stack"},
    {"content": "Fill in the blank: The integral of a constant is a ______.", "course_id": 42, "bloom_level": "Apply", "topic": "Integration", "difficulty": "Easy", "question_type": "Fill in the Blank", "correct_answer": "linear function"},
    {"content": "Fill in the blank: The main character in 'To Kill a Mockingbird' is ______ Finch.", "course_id": 43, "bloom_level": "Remember", "topic": "Characters", "difficulty": "Easy", "question_type": "Fill in the Blank", "correct_answer": "Scout"},
    {"content": "Fill in the blank: The powerhouse of the cell is the ______.", "course_id": 44, "bloom_level": "Remember", "topic": "Cell Biology", "difficulty": "Easy", "question_type": "Fill in the Blank", "correct_answer": "mitochondria"},
    {"content": "Fill in the blank: The formula for water is ______.", "course_id": 45, "bloom_level": "Remember", "topic": "Chemical Formulas", "difficulty": "Easy", "question_type": "Fill in the Blank", "correct_answer": "H2O"},
    {"content": "Write a short essay on the importance of algorithms in computer science.", "course_id": 46, "bloom_level": "Evaluate", "topic": "Algorithms", "difficulty": "Hard", "question_type": "Essay", "essay_details": "The essay should cover the definition of algorithms, their role in problem-solving, and examples of different types of algorithms and their applications."},
    {"content": "Write a short essay on the applications of calculus in engineering.", "course_id": 47, "bloom_level": "Evaluate", "topic": "Calculus", "difficulty": "Hard", "question_type": "Essay", "essay_details": "The essay should discuss the use of calculus in various engineering fields, such as civil, mechanical, and electrical engineering, with specific examples and applications."},
    {"content": "Write a short essay comparing and contrasting the themes of '1984' and 'Brave New World'.", "course_id": 48, "bloom_level": "Evaluate", "topic": "Themes", "difficulty": "Hard", "question_type": "Essay", "essay_details": "The essay should analyze the dystopian themes in both novels, focusing on their similarities and differences, and their relevance to contemporary society."},
    {"content": "Write a short essay on the impact of genetic engineering on modern medicine.", "course_id": 49, "bloom_level": "Evaluate", "topic": "Genetics", "difficulty": "Hard", "question_type": "Essay", "essay_details": "The essay should discuss the advancements in genetic engineering, its applications in medicine, such as gene therapy and CRISPR, and the ethical considerations involved."},
    {"content": "Write a short essay on the significance of green chemistry in sustainable development.", "course_id": 50, "bloom_level": "Evaluate", "topic": "Green Chemistry", "difficulty": "Hard", "question_type": "Essay", "essay_details": "The essay should explain the principles of green chemistry, its role in reducing environmental impact, and examples of green chemistry practices in industry."},
    {"content": "What is the principle of chromatography?", "course_id": 30, "bloom_level": "Remember", "topic": "Separation Techniques", "difficulty": "Easy", "question_type": "Single Correct Answer", "options": "A technique for separating mixtures, A method for synthesizing compounds, A way to measure pH", "correct_answer": "A technique for separating mixtures"},
    {"content": "How does mass spectrometry work?", "course_id": 30, "bloom_level": "Understand", "topic": "Analytical Techniques", "difficulty": "Medium", "question_type": "Single Correct Answer", "options": "By ionizing chemical compounds to measure mass, By separating compounds by boiling points, By detecting chemical reactions", "correct_answer": "By ionizing chemical compounds to measure mass"},
    {"content": "Calculate the concentration of NaCl in a solution if 58.5 grams are dissolved in 1 liter of water.", "course_id": 30, "bloom_level": "Apply", "topic": "Quantitative Analysis", "difficulty": "Medium", "question_type": "Single Correct Answer", "options": "1 M, 2 M, 0.5 M", "correct_answer": "1 M"},
    {"content": "Analyze the accuracy and precision of a set of experimental data: [1.02, 1.01, 1.03, 1.04].", "course_id": 30, "bloom_level": "Analyze", "topic": "Data Interpretation", "difficulty": "Medium", "question_type": "Short Answer", "correct_answer": "The data is precise because the values are close to each other, but accuracy depends on how close the values are to the true value."},
    {"content": "Discuss the importance of calibration in analytical chemistry.", "course_id": 30, "bloom_level": "Evaluate", "topic": "Instrument Calibration", "difficulty": "Hard", "question_type": "Essay", "essay_details": "The essay should explain the role of calibration in ensuring accurate measurements, the methods of calibration, and the consequences of poor calibration."},
    {"content": "What is the purpose of a blank sample in an analytical experiment?", "course_id": 30, "bloom_level": "Remember", "topic": "Experimental Design", "difficulty": "Easy", "question_type": "Single Correct Answer", "options": "To serve as a control, To add more volume, To increase the concentration", "correct_answer": "To serve as a control"},
    {"content": "Explain the difference between accuracy and precision.", "course_id": 30, "bloom_level": "Understand", "topic": "Data Interpretation", "difficulty": "Easy", "question_type": "Short Answer", "correct_answer": "Accuracy refers to how close a measured value is to the true value, while precision refers to the consistency of repeated measurements."},
    {"content": "What is the role of a mobile phase in chromatography?", "course_id": 30, "bloom_level": "Understand", "topic": "Chromatography", "difficulty": "Medium", "question_type": "Single Correct Answer", "options": "To carry the sample through the stationary phase, To react with the sample, To measure the pH", "correct_answer": "To carry the sample through the stationary phase"},
    {"content": "Identify the main components of a mass spectrometer.", "course_id": 30, "bloom_level": "Remember", "topic": "Mass Spectrometry", "difficulty": "Medium", "question_type": "Matching", "pairs": "Ion source:Produces ions, Mass analyzer:Separates ions by mass, Detector:Measures the intensity of ions"},
    {"content": "Describe how UV-Vis spectroscopy is used to determine the concentration of a substance.", "course_id": 30, "bloom_level": "Understand", "topic": "Spectroscopy", "difficulty": "Medium", "question_type": "Short Answer", "correct_answer": "UV-Vis spectroscopy measures the absorbance of light by a substance at specific wavelengths. The absorbance is proportional to the concentration according to Beer's Law."},
    {"content": "Calculate the molarity of a solution if 0.5 moles of solute are dissolved in 2 liters of solution.", "course_id": 30, "bloom_level": "Apply", "topic": "Quantitative Analysis", "difficulty": "Easy", "question_type": "Single Correct Answer", "options": "0.25 M, 1 M, 0.5 M", "correct_answer": "0.25 M"},
    {"content": "What is the principle of Beer's Law?", "course_id": 30, "bloom_level": "Remember", "topic": "Spectroscopy", "difficulty": "Easy", "question_type": "Single Correct Answer", "options": "Absorbance is proportional to concentration, Absorbance is proportional to wavelength, Absorbance is proportional to pH", "correct_answer": "Absorbance is proportional to concentration"},
    {"content": "Differentiate between qualitative and quantitative analysis.", "course_id": 30, "bloom_level": "Understand", "topic": "Analytical Techniques", "difficulty": "Medium", "question_type": "Short Answer", "correct_answer": "Qualitative analysis identifies the components of a sample, while quantitative analysis measures the amount of each component."},
    {"content": "Explain the steps involved in titration.", "course_id": 30, "bloom_level": "Understand", "topic": "Titration", "difficulty": "Medium", "question_type": "Short Answer", "correct_answer": "Titration involves adding a titrant to a sample until the reaction reaches an endpoint, which is often indicated by a color change."},
    {"content": "Identify the uses of gas chromatography.", "course_id": 30, "bloom_level": "Remember", "topic": "Chromatography", "difficulty": "Medium", "question_type": "Short Answer", "correct_answer": "Gas chromatography is used for separating and analyzing compounds that can be vaporized without decomposition."},
    {"content": "Describe the principle of atomic absorption spectroscopy.", "course_id": 30, "bloom_level": "Understand", "topic": "Spectroscopy", "difficulty": "Medium", "question_type": "Short Answer", "correct_answer": "Atomic absorption spectroscopy measures the concentration of elements by detecting the absorption of light by free atoms in the gas phase."},
    {"content": "What is the role of a standard solution in titration?", "course_id": 30, "bloom_level": "Understand", "topic": "Titration", "difficulty": "Easy", "question_type": "Single Correct Answer", "options": "To provide a reference for comparison, To increase the volume of the sample, To change the pH of the solution", "correct_answer": "To provide a reference for comparison"},
    {"content": "Explain the process of sample preparation for gas chromatography.", "course_id": 30, "bloom_level": "Understand", "topic": "Chromatography", "difficulty": "Medium", "question_type": "Short Answer", "correct_answer": "Sample preparation for gas chromatography involves dissolving the sample in a suitable solvent and sometimes derivatizing the sample to make it volatile."},
    {"content": "How is high-performance liquid chromatography (HPLC) different from gas chromatography (GC)?", "course_id": 30, "bloom_level": "Analyze", "topic": "Chromatography", "difficulty": "Medium", "question_type": "Short Answer", "correct_answer": "HPLC uses a liquid mobile phase and is suitable for non-volatile compounds, while GC uses a gas mobile phase and is suitable for volatile compounds."},
    {"content": "Calculate the pH of a solution with a hydrogen ion concentration of 1 x 10^-3 M.", "course_id": 30, "bloom_level": "Apply", "topic": "Quantitative Analysis", "difficulty": "Medium", "question_type": "Single Correct Answer", "options": "3, 1, 7", "correct_answer": "3"},
    {"content": "What is the purpose of using an internal standard in analytical chemistry?", "course_id": 30, "bloom_level": "Understand", "topic": "Experimental Design", "difficulty": "Medium", "question_type": "Single Correct Answer", "options": "To correct for variations in sample preparation and analysis, To increase the sample volume, To change the sample concentration", "correct_answer": "To correct for variations in sample preparation and analysis"},
    {"content": "Discuss the limitations of UV-Vis spectroscopy.", "course_id": 30, "bloom_level": "Evaluate", "topic": "Spectroscopy", "difficulty": "Hard", "question_type": "Short Answer", "correct_answer": "UV-Vis spectroscopy is limited to analyzing compounds that absorb light in the UV-Vis range and cannot provide information about molecular structure."},
    {"content": "Explain the role of a detector in HPLC.", "course_id": 30, "bloom_level": "Understand", "topic": "Chromatography", "difficulty": "Medium", "question_type": "Short Answer", "correct_answer": "The detector in HPLC measures the concentration of eluted compounds by detecting their absorbance or other properties as they pass through the detector."},
    {"content": "What is a calibration curve, and how is it used in quantitative analysis?", "course_id": 30, "bloom_level": "Understand", "topic": "Quantitative Analysis", "difficulty": "Medium", "question_type": "Short Answer", "correct_answer": "A calibration curve is a plot of known concentrations of a substance against the measured response. It is used to determine the concentration of an unknown sample by comparing its response to the curve."},
    {"content": "Describe the principle of thin-layer chromatography (TLC).", "course_id": 30, "bloom_level": "Understand", "topic": "Chromatography", "difficulty": "Medium", "question_type": "Short Answer", "correct_answer": "TLC involves separating compounds based on their affinity for a stationary phase and a mobile phase. The compounds move at different rates, forming distinct spots on the TLC plate."},
    {"content": "How is infrared (IR) spectroscopy used to identify functional groups in a molecule?", "course_id": 30, "bloom_level": "Understand", "topic": "Spectroscopy", "difficulty": "Medium", "question_type": "Short Answer", "correct_answer": "IR spectroscopy measures the absorption of infrared light by a molecule. Different functional groups absorb light at characteristic frequencies, allowing for their identification."},
    {"content": "Calculate the dilution factor if 10 mL of a stock solution is diluted to 100 mL.", "course_id": 30, "bloom_level": "Apply", "topic": "Quantitative Analysis", "difficulty": "Easy", "question_type": "Single Correct Answer", "options": "10, 1, 0.1", "correct_answer": "10"},
    {"content": "Explain the importance of solvent selection in HPLC.", "course_id": 30, "bloom_level": "Understand", "topic": "Chromatography", "difficulty": "Medium", "question_type": "Short Answer", "correct_answer": "Solvent selection in HPLC is important because it affects the separation efficiency, resolution, and retention time of the compounds being analyzed."},
    {"content": "What is the principle of ion-exchange chromatography?", "course_id": 30, "bloom_level": "Understand", "topic": "Chromatography", "difficulty": "Medium", "question_type": "Single Correct Answer", "options": "Separation based on charge, Separation based on size, Separation based on boiling point", "correct_answer": "Separation based on charge"},
    {"content": "Discuss the advantages and disadvantages of using flame atomic absorption spectroscopy (FAAS).", "course_id": 30, "bloom_level": "Evaluate", "topic": "Spectroscopy", "difficulty": "Hard", "question_type": "Short Answer", "correct_answer": "Advantages of FAAS include high sensitivity and selectivity for metal analysis. Disadvantages include the need for a flame source and potential interference from other elements."},
    {"content": "Describe the process of preparing a sample for atomic absorption spectroscopy (AAS).", "course_id": 30, "bloom_level": "Understand", "topic": "Sample Preparation", "difficulty": "Medium", "question_type": "Short Answer", "correct_answer": "Sample preparation for AAS involves dissolving the sample in an appropriate solvent and possibly diluting it to fall within the instrument's detection range."},
    {"content": "What are the key differences between absorption and emission spectroscopies?", "course_id": 30, "bloom_level": "Understand", "topic": "Spectroscopy", "difficulty": "Medium", "question_type": "Short Answer", "correct_answer": "Absorption spectroscopy measures the absorption of light by a sample, while emission spectroscopy measures the light emitted by a sample after excitation."},
    {"content": "Calculate the molality of a solution if 5 grams of NaCl are dissolved in 500 grams of water.", "course_id": 30, "bloom_level": "Apply", "topic": "Quantitative Analysis", "difficulty": "Medium", "question_type": "Single Correct Answer", "options": "0.171 mol/kg, 0.5 mol/kg, 0.1 mol/kg", "correct_answer": "0.171 mol/kg"},
    {"content": "Explain the principle of fluorescence spectroscopy.", "course_id": 30, "bloom_level": "Understand", "topic": "Spectroscopy", "difficulty": "Medium", "question_type": "Short Answer", "correct_answer": "Fluorescence spectroscopy measures the emission of light by a substance that has absorbed light or other electromagnetic radiation. The emitted light is usually at a longer wavelength than the absorbed light."},
    {"content": "What are the components of an HPLC system?", "course_id": 30, "bloom_level": "Remember", "topic": "Chromatography", "difficulty": "Medium", "question_type": "Matching", "pairs": "Pump:Moves the mobile phase through the system, Injector:Introduces the sample into the mobile phase, Column:Separates the sample components, Detector:Detects the separated components"},
    {"content": "Discuss the role of retention time in gas chromatography.", "course_id": 30, "bloom_level": "Understand", "topic": "Chromatography", "difficulty": "Medium", "question_type": "Short Answer", "correct_answer": "Retention time is the time it takes for a compound to travel through the chromatography column to the detector. It is used to help identify compounds based on their interaction with the stationary and mobile phases."},
    {"content": "Explain the concept of partition coefficient in chromatography.", "course_id": 30, "bloom_level": "Understand", "topic": "Chromatography", "difficulty": "Medium", "question_type": "Short Answer", "correct_answer": "The partition coefficient is the ratio of concentrations of a compound in the stationary phase to the mobile phase. It indicates how a compound is distributed between the two phases and affects its retention time."},
    {"content": "Calculate the percentage error if the measured value is 10.2 and the true value is 10.", "course_id": 30, "bloom_level": "Apply", "topic": "Quantitative Analysis", "difficulty": "Easy", "question_type": "Single Correct Answer", "options": "2%, 0.2%, 1%", "correct_answer": "2%"},
    {"content": "What is the principle of ion mobility spectrometry (IMS)?", "course_id": 30, "bloom_level": "Understand", "topic": "Analytical Techniques", "difficulty": "Medium", "question_type": "Short Answer", "correct_answer": "Ion mobility spectrometry separates ions based on their velocity in a gas under the influence of an electric field, which depends on their size, shape, and charge."},
    {"content": "Discuss the applications of Raman spectroscopy in chemical analysis.", "course_id": 30, "bloom_level": "Evaluate", "topic": "Spectroscopy", "difficulty": "Hard", "question_type": "Short Answer", "correct_answer": "Raman spectroscopy is used for identifying molecular structures, characterizing materials, and studying chemical bonding and reactions. It is non-destructive and can analyze samples in various states."},
    {"content": "Describe the difference between HPLC and UHPLC.", "course_id": 30, "bloom_level": "Understand", "topic": "Chromatography", "difficulty": "Medium", "question_type": "Short Answer", "correct_answer": "UHPLC (Ultra-High Performance Liquid Chromatography) operates at higher pressures than HPLC, providing faster and more efficient separations with better resolution."},
    {"content": "What are the advantages of using capillary electrophoresis (CE) in analytical chemistry?", "course_id": 30, "bloom_level": "Evaluate", "topic": "Electrophoresis", "difficulty": "Hard", "question_type": "Short Answer", "correct_answer": "Advantages of CE include high resolution, rapid analysis, low sample and reagent consumption, and the ability to separate a wide range of analytes."},
    {"content": "Calculate the concentration of HCl if 50 mL of 0.1 M NaOH neutralizes 25 mL of HCl.", "course_id": 30, "bloom_level": "Apply", "topic": "Quantitative Analysis", "difficulty": "Medium", "question_type": "Single Correct Answer", "options": "0.2 M, 0.1 M, 0.05 M", "correct_answer": "0.2 M"},
    {"content": "Explain the role of a carrier gas in gas chromatography.", "course_id": 30, "bloom_level": "Understand", "topic": "Chromatography", "difficulty": "Medium", "question_type": "Short Answer", "correct_answer": "The carrier gas in gas chromatography transports the sample vapor through the column. It should be inert and of high purity to avoid reactions with the sample."},
    {"content": "What is the principle of X-ray fluorescence (XRF) spectroscopy?", "course_id": 30, "bloom_level": "Understand", "topic": "Spectroscopy", "difficulty": "Medium", "question_type": "Short Answer", "correct_answer": "XRF spectroscopy measures the fluorescent X-rays emitted by a material when it is excited by an X-ray source. The emitted X-rays are characteristic of the elements present in the sample."},
    {"content": "Discuss the use of reference standards in analytical chemistry.", "course_id": 30, "bloom_level": "Evaluate", "topic": "Experimental Design", "difficulty": "Hard", "question_type": "Short Answer", "correct_answer": "Reference standards are used to ensure the accuracy and reliability of analytical measurements by providing a known reference for comparison. They help in calibrating instruments and validating methods."},
    {"content": "Calculate the mass percent of NaCl in a solution if 20 grams of NaCl are dissolved in 80 grams of water.", "course_id": 30, "bloom_level": "Apply", "topic": "Quantitative Analysis", "difficulty": "Medium", "question_type": "Single Correct Answer", "options": "20%, 25%, 50%", "correct_answer": "20%"},
    {"content": "Explain the concept of limit of detection (LOD) in analytical chemistry.", "course_id": 30, "bloom_level": "Understand", "topic": "Analytical Techniques", "difficulty": "Medium", "question_type": "Short Answer", "correct_answer": "The limit of detection is the lowest concentration of an analyte that can be reliably detected but not necessarily quantified. It is important for determining the sensitivity of an analytical method."},
    {"content": "What are the main differences between FTIR and dispersive IR spectroscopy?", "course_id": 30, "bloom_level": "Understand", "topic": "Spectroscopy", "difficulty": "Medium", "question_type": "Short Answer", "correct_answer": "FTIR (Fourier Transform Infrared) spectroscopy uses an interferometer to collect all wavelengths simultaneously, providing faster and more sensitive measurements compared to dispersive IR, which uses a monochromator to isolate individual wavelengths."},
    {"content": "Discuss the importance of sample homogeneity in analytical chemistry.", "course_id": 30, "bloom_level": "Evaluate", "topic": "Sample Preparation", "difficulty": "Hard", "question_type": "Short Answer", "correct_answer": "Sample homogeneity is crucial for obtaining accurate and reproducible results in analytical chemistry. Inhomogeneous samples can lead to variability in measurements and unreliable data."},
    {"content": "Explain the process of gravimetric analysis.", "course_id": 30, "bloom_level": "Understand", "topic": "Quantitative Analysis", "difficulty": "Medium", "question_type": "Short Answer", "correct_answer": "Gravimetric analysis involves measuring the mass of an analyte or its derivative to determine the analyte's concentration. It typically involves precipitation, filtration, drying, and weighing."},
    {"content": "What is the principle of inductively coupled plasma (ICP) spectroscopy?", "course_id": 30, "bloom_level": "Understand", "topic": "Spectroscopy", "difficulty": "Medium", "question_type": "Short Answer", "correct_answer": "ICP spectroscopy uses a high-temperature plasma to excite atoms and ions in a sample, causing them to emit light at characteristic wavelengths. The emitted light is measured to determine the elemental composition of the sample."},
    {"content": "Calculate the normality of a solution if 1 equivalent of solute is dissolved in 2 liters of solution.", "course_id": 30, "bloom_level": "Apply", "topic": "Quantitative Analysis", "difficulty": "Easy", "question_type": "Single Correct Answer", "options": "0.5 N, 1 N, 2 N", "correct_answer": "0.5 N"},
    {"content": "Describe the role of a stationary phase in chromatography.", "course_id": 30, "bloom_level": "Understand", "topic": "Chromatography", "difficulty": "Medium", "question_type": "Short Answer", "correct_answer": "The stationary phase in chromatography is the material that remains fixed in place while the mobile phase moves through it. It interacts with the sample components, causing them to separate based on their affinity for the stationary phase."},
    {"content": "Discuss the applications of electrochemical sensors in analytical chemistry.", "course_id": 30, "bloom_level": "Evaluate", "topic": "Electrochemistry", "difficulty": "Hard", "question_type": "Short Answer", "correct_answer": "Electrochemical sensors are used for detecting and measuring chemical species in various environments, including environmental monitoring, medical diagnostics, and industrial process control. They offer high sensitivity and selectivity."},
    {"content": "Explain the concept of partition chromatography.", "course_id": 30, "bloom_level": "Understand", "topic": "Chromatography", "difficulty": "Medium", "question_type": "Short Answer", "correct_answer": "Partition chromatography separates compounds based on their partitioning between a liquid stationary phase and a liquid or gas mobile phase. The separation is based on the differing solubilities of the compounds in the two phases."},
    {"content": "Calculate the dilution factor if 5 mL of a stock solution is diluted to 250 mL.", "course_id": 30, "bloom_level": "Apply", "topic": "Quantitative Analysis", "difficulty": "Easy", "question_type": "Single Correct Answer", "options": "50, 25, 5", "correct_answer": "50"},
    {"content": "What is the principle of potentiometric titration?", "course_id": 30, "bloom_level": "Understand", "topic": "Titration", "difficulty": "Medium", "question_type": "Single Correct Answer", "options": "Measurement of potential to determine endpoint, Measurement of color change to determine endpoint, Measurement of pH to determine endpoint", "correct_answer": "Measurement of potential to determine endpoint"},
    {"content": "Discuss the importance of method validation in analytical chemistry.", "course_id": 30, "bloom_level": "Evaluate", "topic": "Method Validation", "difficulty": "Hard", "question_type": "Short Answer", "correct_answer": "Method validation ensures that an analytical method is suitable for its intended purpose, providing accurate, reliable, and reproducible results. It involves evaluating parameters such as precision, accuracy, specificity, and robustness."},
    {"content": "Explain the difference between primary and secondary standards in titration.", "course_id": 30, "bloom_level": "Understand", "topic": "Titration", "difficulty": "Medium", "question_type": "Short Answer", "correct_answer": "Primary standards are pure, stable compounds with known concentration used to calibrate solutions. Secondary standards are solutions whose concentrations are determined by titration against primary standards."},
    {"content": "What are the main components of a UV-Vis spectrophotometer?", "course_id": 30, "bloom_level": "Remember", "topic": "Spectroscopy", "difficulty": "Medium", "question_type": "Matching", "pairs": "Light source:Provides the light, Monochromator:Selects specific wavelengths, Sample holder:Holds the sample, Detector:Measures the absorbance"},
    {"content": "Calculate the concentration of a solution if 2 grams of solute are dissolved in 100 mL of solution.", "course_id": 30, "bloom_level": "Apply", "topic": "Quantitative Analysis", "difficulty": "Easy", "question_type": "Single Correct Answer", "options": "0.02 g/mL, 0.2 g/mL, 2 g/mL", "correct_answer": "0.02 g/mL"},
    {"content": "Explain the role of temperature in gas chromatography.", "course_id": 30, "bloom_level": "Understand", "topic": "Chromatography", "difficulty": "Medium", "question_type": "Short Answer", "correct_answer": "Temperature in gas chromatography affects the volatility of the sample components and their interaction with the stationary phase. It influences the retention time and separation efficiency."},
    {"content": "Discuss the applications of inductively coupled plasma mass spectrometry (ICP-MS).", "course_id": 30, "bloom_level": "Evaluate", "topic": "Spectroscopy", "difficulty": "Hard", "question_type": "Short Answer", "correct_answer": "ICP-MS is used for trace element analysis, environmental testing, food safety, and medical diagnostics. It offers high sensitivity and the ability to analyze multiple elements simultaneously."},
    {"content": "What is the principle of electrochemical impedance spectroscopy (EIS)?", "course_id": 30, "bloom_level": "Understand", "topic": "Electrochemistry", "difficulty": "Medium", "question_type": "Short Answer", "correct_answer": "EIS measures the impedance of a system over a range of frequencies to study the electrochemical properties of materials, including charge transfer resistance and double-layer capacitance."},
    {"content": "Calculate the molarity of a solution if 3 moles of solute are dissolved in 6 liters of solution.", "course_id": 30, "bloom_level": "Apply", "topic": "Quantitative Analysis", "difficulty": "Easy", "question_type": "Single Correct Answer", "options": "0.5 M, 1 M, 2 M", "correct_answer": "0.5 M"},
    {"content": "Explain the importance of pH control in analytical chemistry.", "course_id": 30, "bloom_level": "Understand", "topic": "Experimental Design", "difficulty": "Medium", "question_type": "Short Answer", "correct_answer": "pH control is crucial because it affects the solubility, stability, and reactivity of analytes. It ensures consistent and accurate analytical measurements, particularly in techniques like chromatography and spectrophotometry."},
    {"content": "What are the main differences between qualitative and quantitative spectroscopy?", "course_id": 30, "bloom_level": "Understand", "topic": "Spectroscopy", "difficulty": "Medium", "question_type": "Short Answer", "correct_answer": "Qualitative spectroscopy identifies the presence of elements or compounds, while quantitative spectroscopy measures their concentration."},
    {"content": "Discuss the use of solid-phase extraction (SPE) in sample preparation.", "course_id": 30, "bloom_level": "Evaluate", "topic": "Sample Preparation", "difficulty": "Hard", "question_type": "Short Answer", "correct_answer": "SPE is used to isolate and concentrate analytes from complex matrices. It improves detection limits and reduces interferences in subsequent analyses, making it valuable for environmental, clinical, and pharmaceutical applications."},
    {"content": "Explain the concept of chemical shift in NMR spectroscopy.", "course_id": 30, "bloom_level": "Understand", "topic": "Spectroscopy", "difficulty": "Medium", "question_type": "Short Answer", "correct_answer": "Chemical shift in NMR spectroscopy refers to the resonant frequency of a nucleus relative to a reference standard. It provides information about the chemical environment of the nuclei and helps identify functional groups."},
    {"content": "Calculate the molarity of a solution if 4 grams of NaOH (molar mass = 40 g/mol) are dissolved in 500 mL of water.", "course_id": 30, "bloom_level": "Apply", "topic": "Quantitative Analysis", "difficulty": "Medium", "question_type": "Single Correct Answer", "options": "0.2 M, 0.1 M, 0.4 M", "correct_answer": "0.2 M"},
    {"content": "What is the principle of mass spectrometry?", "course_id": 30, "bloom_level": "Understand", "topic": "Analytical Techniques", "difficulty": "Medium", "question_type": "Short Answer", "correct_answer": "Mass spectrometry measures the mass-to-charge ratio of ions to identify and quantify molecules. It involves ionizing the sample, separating ions based on their mass, and detecting the ions to produce a spectrum."},
    {"content": "Discuss the applications of thermogravimetric analysis (TGA) in materials science.", "course_id": 30, "bloom_level": "Evaluate", "topic": "Thermal Analysis", "difficulty": "Hard", "question_type": "Short Answer", "correct_answer": "TGA measures changes in mass as a function of temperature. It is used to study thermal stability, composition, and decomposition of materials, providing valuable information for material development and quality control."},
    {"content": "Explain the difference between ion-selective electrodes and reference electrodes.", "course_id": 30, "bloom_level": "Understand", "topic": "Electrochemistry", "difficulty": "Medium", "question_type": "Short Answer", "correct_answer": "Ion-selective electrodes respond selectively to specific ions, while reference electrodes provide a stable potential against which the measurement is made. Both are essential for accurate electrochemical measurements."},
    {"content": "Calculate the molality of a solution if 10 grams of KCl (molar mass = 74.5 g/mol) are dissolved in 250 grams of water.", "course_id": 30, "bloom_level": "Apply", "topic": "Quantitative Analysis", "difficulty": "Medium", "question_type": "Single Correct Answer", "options": "0.54 mol/kg, 0.67 mol/kg, 0.27 mol/kg", "correct_answer": "0.54 mol/kg"},
    {"content": "What is the principle of thermal conductivity detectors in gas chromatography?", "course_id": 30, "bloom_level": "Understand", "topic": "Chromatography", "difficulty": "Medium", "question_type": "Short Answer", "correct_answer": "Thermal conductivity detectors measure changes in the thermal conductivity of the carrier gas caused by the presence of analytes. The change in thermal conductivity is proportional to the concentration of analytes."},
    {"content": "Discuss the use of microwave digestion in sample preparation.", "course_id": 30, "bloom_level": "Evaluate", "topic": "Sample Preparation", "difficulty": "Hard", "question_type": "Short Answer", "correct_answer": "Microwave digestion uses microwave energy to rapidly heat and digest samples in a closed vessel. It is efficient and reduces sample preparation time, making it valuable for elemental analysis in various fields."},
    {"content": "Explain the concept of isocratic and gradient elution in HPLC.", "course_id": 30, "bloom_level": "Understand", "topic": "Chromatography", "difficulty": "Medium", "question_type": "Short Answer", "correct_answer": "Isocratic elution uses a constant mobile phase composition throughout the analysis, while gradient elution changes the mobile phase composition over time to improve separation efficiency."},
    {"content": "Calculate the molarity of a solution if 5 grams of glucose (molar mass = 180 g/mol) are dissolved in 1 liter of water.", "course_id": 30, "bloom_level": "Apply", "topic": "Quantitative Analysis", "difficulty": "Medium", "question_type": "Single Correct Answer", "options": "0.0278 M, 0.0556 M, 0.1111 M", "correct_answer": "0.0278 M"},
    {"content": "What is the principle of gas-liquid chromatography (GLC)?", "course_id": 30, "bloom_level": "Understand", "topic": "Chromatography", "difficulty": "Medium", "question_type": "Short Answer", "correct_answer": "Gas-liquid chromatography separates compounds based on their partitioning between a stationary liquid phase and a mobile gas phase. The separation is influenced by the volatility and interaction of compounds with the liquid phase."},
    {"content": "Discuss the applications of differential scanning calorimetry (DSC) in polymer analysis.", "course_id": 30, "bloom_level": "Evaluate", "topic": "Thermal Analysis", "difficulty": "Hard", "question_type": "Short Answer", "correct_answer": "DSC measures heat flow associated with phase transitions in polymers. It is used to study melting, crystallization, glass transition, and thermal stability, providing insights into polymer properties and processing."}
]

with app.app_context():
    # Delete all existing courses, course outcomes, and questions
    CourseOutcome.query.delete()
    Question.query.delete()
    Course.query.delete()
    db.session.commit()
    
    # Insert new courses and their outcomes
    for course in courses:
        new_course = Course(
            course_code=course["course_code"],
            name=course["name"],
            school=course["school"],
            department=course["department"]
        )
        db.session.add(new_course)
        db.session.commit()
        
        for outcome in course["outcomes"]:
            new_outcome = CourseOutcome(
                number=outcome["number"],
                description=outcome["description"],
                course_id=new_course.id
            )
            db.session.add(new_outcome)
        db.session.commit()
    
    n = len(courses)
    # Insert new questions
    for question in questions:
        course_id=question["course_id"]
        if course_id > n:
            course_id = random.randint(1, n)
        new_question = Question(
            content=question["content"],
            course_id=course_id,
            bloom_level=question["bloom_level"],
            topic=question["topic"],
            difficulty=question["difficulty"],
            question_type=question["question_type"],
            options=question.get("options"),
            correct_answer=question.get("correct_answer"),
            created_by="Dummy User"
        )
        db.session.add(new_question)
    db.session.commit()
    print("Dummy data inserted successfully!")