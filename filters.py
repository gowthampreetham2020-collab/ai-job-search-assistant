def filter_jobs(jobs, location=None):
    filtered = []

    for job in jobs:
        if location and location.lower() not in job.lower():
            continue
        filtered.append(job)

    return filtered
