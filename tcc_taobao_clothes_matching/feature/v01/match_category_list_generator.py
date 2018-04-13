"""
根据比例生成category pair

"""
import pandas as pd

from core.config import *

# default
THRESHOLD = 1


def filter(d, threshold=THRESHOLD):
    if threshold != 1:
        for key in d:
            divider = int(len(d[key]) * threshold)
            d[key] = d[key][:divider]
            d[key] = sorted(d[key])

    return d


def generate_match_list_by_match(threshold=THRESHOLD):
    cate_pair = pd.read_csv(file_ft_category_match_rate_by_match)
    cate_pair = cate_pair[['item_category_x', 'item_category_y']]

    d = {}
    for val in cate_pair.values:
        if val[0] not in d:
            d[val[0]] = []
        d[val[0]].append(val[1])
        if val[1] not in d:
            d[val[1]] = []
        d[val[1]].append(val[0])

    d = filter(d, threshold)

    return d


def generate_match_list_by_all(threshold=THRESHOLD):
    cate_pair = pd.read_csv(file_ft_category_match_rate_by_all)
    cate_pair = cate_pair[['item_category_x', 'item_category_y']]

    d = {}
    for val in cate_pair.values:
        if val[0] not in d:
            d[val[0]] = []
        d[val[0]].append(val[1])

    d = filter(d, threshold)

    return d


if __name__ == '__main__':
    d = generate_match_list_by_all(0.2)

    for key in d:
        print(key, d[key])
