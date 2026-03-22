<<<<<<< HEAD
SKILLS = [
    "python",
    "sql",
    "machine learning",
    "aws",
    "docker",
    "java",
    "data analysis"
]

def detect_skills(text):

    found = []

    for skill in SKILLS:

        if skill in text.lower():
            found.append(skill)

=======
SKILLS = [
    "python",
    "sql",
    "machine learning",
    "aws",
    "docker",
    "java",
    "data analysis"
]

def detect_skills(text):

    found = []

    for skill in SKILLS:

        if skill in text.lower():
            found.append(skill)

>>>>>>> e964efba0d8a6b86fee83d400bb44c95b9fe409f
    return found