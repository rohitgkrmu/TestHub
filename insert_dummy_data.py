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
    {"content": "Write a short essay on the significance of green chemistry in sustainable development.", "course_id": 50, "bloom_level": "Evaluate", "topic": "Green Chemistry", "difficulty": "Hard", "question_type": "Essay", "essay_details": "The essay should explain the principles of green chemistry, its role in reducing environmental impact, and examples of green chemistry practices in industry."}

]

with app.app_context():
    # Delete all existing courses, course outcomes, and questions
    CourseOutcome.query.delete()
    Question.query.delete()
    Course.query.delete()
    db.session.commit()

    print(len(courses))
    
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