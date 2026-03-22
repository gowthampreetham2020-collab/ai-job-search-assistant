
def extract_salary(text):

    import re

    match = re.search(r"\d+\s*-\s*\d+\s*LPA", text)

    if match:
        return match.group()


def extract_salary(text):
    import re
    match = re.search(r"\d+\s*-\s*\d+\s*LPA", text)
    if match:
        return match.group()
    return "Not listed"
