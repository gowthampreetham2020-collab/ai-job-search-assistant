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

    return found