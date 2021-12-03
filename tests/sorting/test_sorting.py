from src.sorting import sort_by

# 'max_salary', 'min_salary', 'date_posted' list_date_posted
list_salary = [
    {"min_salary": 1000, "max_salary": 3500, "date_posted": "2021-01-01"},
    {"min_salary": 2000, "max_salary": 6500, "date_posted": "2021-01-01"},
    {"min_salary": 3000, "max_salary": 8500, "date_posted": "2021-01-01"},
]

list_max_salary = [
    {"min_salary": 5000, "max_salary": 15500, "date_posted": "2021-01-01"},
    {"min_salary": 4000, "max_salary": 10500, "date_posted": "2021-01-01"},
    {"min_salary": 3000, "max_salary": 8500, "date_posted": "2021-01-01"},
]
list_min_salary = [
    {"min_salary": 1000, "max_salary": 3500, "date_posted": "2021-01-01"},
    {"min_salary": 2000, "max_salary": 6500, "date_posted": "2021-01-01"},
    {"min_salary": 3000, "max_salary": 8500, "date_posted": "2021-01-01"},
]


def test_sort_by_criteria():
    assert sort_by(list_salary, 'min_salary') == list_min_salary
    assert sort_by(list_salary, 'max_salary') == list_max_salary
    assert sort_by(list_salary, 'date_posted') == list_max_salary
