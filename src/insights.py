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
    job_industry_list = list()

    for job in jobs:
        if job['industry'] == industry:
            job_industry_list.append(job)
    return job_industry_list


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
    if (
      "min_salary" not in job.keys() or
      "max_salary" not in job.keys() or
      type(job["min_salary"]) != int or
      type(job["max_salary"]) != int or
      job["min_salary"] > job["max_salary"] or
      type(salary) != int
    ):
        raise ValueError
    if job["min_salary"] <= salary <= job["max_salary"]:
        return True
    else:
        return False


def filter_by_salary_range(jobs, salary):
    salary_range_list = list()

    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                salary_range_list.append(job)
        except ValueError:
            pass
    return salary_range_list
