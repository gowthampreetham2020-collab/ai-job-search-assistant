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

    text = text.lower()
    found = []

    for skill in SKILLS:
        if skill in text:
            found.append(skill)

    return found