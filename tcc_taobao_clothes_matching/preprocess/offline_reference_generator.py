"""
线下验证集生成
1. 随机抽样 match item_set 中的 reference_count(5462) 个 item
2. 对 reference_count 根据匹配生成匹配
"""

import pandas as pd

from core.config import *
from util.pickle_utils import dump_pickle


def get_match_list(item_set, pairs):
    """
    生成匹配序列
    dict_item = {item1: [item11, ...], item2: [item21, ...]}
    """
    # 初始化
    dict_item = {}
    for item in item_set.values:
        dict_item[item] = []

    for val in pairs.values:
        if val[0] in dict_item:
            dict_item[val[0]].append(val[1])
        if val[1] in dict_item:
            dict_item[val[1]].append(val[0])

    return dict_item


if __name__ == '__main__':
    match_pair = pd.read_csv(file_dim_fashion_matchsets)
    reference_set = pd.read_csv(file_offline_train_item)
    reference_set = reference_set['item_id']

    # 删除不含测试商品的匹配对
    include_row = match_pair['item_id_x'].isin(reference_set) | match_pair['item_id_y'].isin(reference_set)
    match_pair = match_pair[include_row]

    # step 2. 生成匹配对
    match_list = get_match_list(reference_set, match_pair)
    for key in match_list:
        print(key, match_list[key])
    # step 3. 保存到文件
    dump_pickle(match_list, file_offline_reference_data_pickle)
