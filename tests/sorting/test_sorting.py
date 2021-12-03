from src.sorting import sort_by
import pytest


list_salary = [
    {"date_posted": "2021-01-01", "max_salary": 6500, "min_salary": 2000},
    {"date_posted": "2021-02-01", "max_salary": 3500, "min_salary": 1000},
    {"date_posted": "2021-03-01", "max_salary": 8500, "min_salary": 3000},
]

list_min_salary = [list_salary[1], list_salary[0], list_salary[2]]
list_max_salary = [list_salary[2], list_salary[0], list_salary[1]]
list_date_posted = [list_salary[2], list_salary[1], list_salary[0]]


def test_sort_by_criteria():
    sort_by(list_salary, "min_salary")
    assert list_salary == list_min_salary
    # /n
    # result = sort_by(list_salary, "min_salary")
    # assert result == list_min_salary
    sort_by(list_salary, "max_salary")
    assert list_salary == list_max_salary
    sort_by(list_salary, "date_posted")
    assert list_salary == list_date_posted

    with pytest.raises(ValueError, match="invalid sorting criteria: oi bobo"):
        sort_by(list_salary, "oi bobo")
