<<<<<<< HEAD
def filter_jobs(jobs, location=None):

    filtered = []

    for job in jobs:

        if location and location.lower() not in job.lower():
            continue

        filtered.append(job)

=======
def filter_jobs(jobs, location=None):

    filtered = []

    for job in jobs:

        if location and location.lower() not in job.lower():
            continue

        filtered.append(job)

>>>>>>> e964efba0d8a6b86fee83d400bb44c95b9fe409f
    return filtered