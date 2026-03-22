<<<<<<< HEAD
def extract_salary(text):

    import re

    match = re.search(r"\d+\s*-\s*\d+\s*LPA", text)

    if match:
        return match.group()

=======
def extract_salary(text):

    import re

    match = re.search(r"\d+\s*-\s*\d+\s*LPA", text)

    if match:
        return match.group()

>>>>>>> e964efba0d8a6b86fee83d400bb44c95b9fe409f
    return "Not listed"