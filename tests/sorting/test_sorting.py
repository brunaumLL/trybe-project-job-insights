from src.sorting import sort_by


def jobs():
    return [
        {
            "title": "Bad_Job",
            "min_salary": "0",
            "max_salary": "50",
            "date_posted": "2023-01-23"
        },
        {
            "title": "Just_a_Job",
            "min_salary": "55",
            "max_salary": "100",
            "date_posted": "2023-02-01"
        },
        {
            "title": "Good_Job",
            "min_salary": "60",
            "max_salary": "200",
            "date_posted": "2023-01-10"
        },
    ]


def test_sort_by_criteria():
    job = jobs()
    criteria = ["min_salary", "max_salary", "date_posted"]

    for c in criteria:
        sort_by(job, c)
        first_job = job[0]["title"]
        last_job = job[-1]["title"]

        if c == "min_salary":
            assert first_job == "Bad_Job"
            assert last_job == "Good_Job"
        if c == "max_salary":
            assert first_job == "Good_Job"
            assert last_job == "Bad_Job"
        if c == "date_posted":
            assert first_job == "Just_a_Job"
            assert last_job == "Good_Job"
