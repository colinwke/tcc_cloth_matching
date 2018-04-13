"""
线下评测
输入为字典

dict = {
    item1: [item11, item12, ...]
    item2: [item21, item22, ...]
}
"""

from math import log

from util.pickle_utils import load_pickle

from core.config import *


def _calc_api_200(list_reference, list_predict):
    n = len(list_reference)
    sum = 0

    # 找到相同的元素
    correct_count = 0
    for i, val in enumerate(list_predict):
        if val in list_reference:
            correct_count += 1
            pk = log(correct_count / (i + 1))
            sum += 1 / (1 - pk)

    return sum / n


def _calc_map_200(reference, predict, commit):
    sum = 0
    miss_count = 0
    for i in reference:
        if i not in predict:
            miss_count += 1
            continue
        match_list = predict[i]
        if (commit is True) & (len(match_list) > 200):
            match_list = match_list[:200]
        sum += _calc_api_200(reference[i], match_list)

    print('miss count:', miss_count)

    return sum / len(reference)


def evaluate(predict, commit=True):
    reference = load_pickle(file_offline_reference_data_pickle)
    score = _calc_map_200(reference, predict, commit)
    print('map@200: %.8f%%' % (score * 100))


def save_commit(predict):
    f = open(file_online_commit, 'w')

    content = ''
    for key in predict:
        match_list = predict[key]
        # 选取前200个商品
        if len(match_list) > 200:
            match_list = match_list[:200]

        match_list = list(map(str, match_list))
        content = content + str(key) + ' ' + ','.join(match_list) + '\n'

    f.write(content)
    f.close()


if __name__ == '__main__':
    predict = load_pickle(file_offline_reference_data_pickle)
    evaluate(predict)
