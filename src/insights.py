from .jobs import read


def get_unique_job_types(path):
    result = set()
    jobs_dict = read(path)
    for dict in jobs_dict:
        result.add(dict['job_type'])

    return list(result)


def filter_by_job_type(jobs, job_type):
    result = []
    for dict in jobs:
        if dict['job_type'] == job_type:
            result.append(dict)
    return result


def get_unique_industries(path):
    result = set()
    jobs_dict = read(path)
    for dict in jobs_dict:
        if dict['industry']:
            result.add(dict['industry'])

    return list(result)


def filter_by_industry(jobs, industry):
    result = []
    for dict in jobs:
        if dict['industry'] == industry:
            result.append(dict)
    return result


def get_max_salary(path):
    result = set()
    jobs_dict = read(path)
    for dict in jobs_dict:
        if dict['max_salary'].isnumeric():
            result.add(int(dict['max_salary']))

    return max(list(result))

# isnumeric
#  https://www.programiz.com/python-programming/methods/string/isnumeric


def get_min_salary(path):
    result = set()
    jobs_dict = read(path)
    for dict in jobs_dict:
        if dict['min_salary'].isnumeric():
            result.add(int(dict['min_salary']))

    return min(list(result))


def matches_salary_range(job, salary):

    if ('max_salary' not in job or 'min_salary' not in job):
        raise ValueError('Error')

    is_not_valid = (
        not isinstance(salary, int)
        or not isinstance(job['max_salary'], int)
        or not isinstance(job['min_salary'], int)
        or job['min_salary'] > job['max_salary']
        )

    if is_not_valid:
        raise ValueError('Error')

    if job['min_salary'] <= salary <= job['max_salary']:
        return True
    else:
        return False


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
