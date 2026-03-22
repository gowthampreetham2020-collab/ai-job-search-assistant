skills = [
"python",
"sql",
"machine learning",
"aws",
"docker"
]

def detect_skills(text):

    found = []

    for skill in skills:

        if skill in text.lower():
            found.append(skill)

    return found