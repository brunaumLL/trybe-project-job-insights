from src.brazilian_jobs import read_brazilian_file


def test_brazilian_jobs():
    path = 'tests/mocks/brazilians_jobs.csv'
    dicts = read_brazilian_file(path)

    for dict in dicts:
        title = "title" in dict.keys()
        salary = "salary" in dict.keys()
        type = "type" in dict.keys()

        assert title is True
        assert salary is True
        assert type is True
