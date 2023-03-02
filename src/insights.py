from src.jobs import read


def get_unique_job_types(path):
    jobs = read(path)
    unique_jobs_type = set()

    for job in jobs:
        all_jobs_type = job['job_type']
        unique_jobs_type.add(all_jobs_type)
    return unique_jobs_type


def filter_by_job_type(jobs, job_type):
    job_type_list = list()

    for job in jobs:
        if job['job_type'] == job_type:
            job_type_list.append(job)
    return job_type_list


def get_unique_industries(path):
    jobs = read(path)
    unique_industries = set()

    for job in jobs:
        if job['industry']:
            all_industries = job['industry']
            unique_industries.add(all_industries)
    print(unique_industries)
    return unique_industries


def filter_by_industry(jobs, industry):
    """Filters a list of jobs by industry

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    industry : str
        Industry for the list filter

    Returns
    -------
    list
        List of jobs with provided industry
    """
    return []


def get_max_salary(path):
    jobs = read(path)
    max_salary = set()

    for job in jobs:
        if job['max_salary'].isnumeric():
            all_salary = int(job['max_salary'])
            max_salary.add(all_salary)
    return max(max_salary)


def get_min_salary(path):
    jobs = read(path)
    min_salary = set()

    for job in jobs:
        if job['min_salary'].isnumeric():
            all_salary = int(job['min_salary'])
            min_salary.add(all_salary)
    return min(min_salary)


def matches_salary_range(job, salary):
    """Checks if a given salary is in the salary range of a given job

    Parameters
    ----------
    job : dict
        The job with `min_salary` and `max_salary` keys
    salary : int
        The salary to check if matches with salary range of the job

    Returns
    -------
    bool
        True if the salary is in the salary range of the job, False otherwise

    Raises
    ------
    ValueError
        If `job["min_salary"]` or `job["max_salary"]` doesn't exists
        If `job["min_salary"]` or `job["max_salary"]` aren't valid integers
        If `job["min_salary"]` is greather than `job["max_salary"]`
        If `salary` isn't a valid integer
    """
    pass


def filter_by_salary_range(jobs, salary):
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    return []
