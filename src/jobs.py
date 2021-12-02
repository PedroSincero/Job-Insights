from functools import lru_cache
import csv


@lru_cache
def read(path):
    with open(path) as file:
        result = []
        jobs_dict = csv.DictReader(file)
        for dict in jobs_dict:
            result.append(dict)
    return result
