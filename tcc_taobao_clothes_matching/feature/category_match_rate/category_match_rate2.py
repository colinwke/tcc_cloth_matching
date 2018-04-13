"""
计算类别之间的匹配率
数据来源于已经匹配好的商品
计算公式：match_rate = (a intersection b) / (a union b)
"""

import pandas as pd

from core.config import *


def add_item_category(match_item_pair):
    item_info = pd.read_csv(file_dim_items)

    match_item_pair = pd.merge(match_item_pair, item_info, how='left', left_on='item_id_x', right_on='item_id')
    match_item_pair = pd.merge(match_item_pair, item_info, how='left', left_on='item_id_y', right_on='item_id')
    match_item_pair = match_item_pair[['item_id_x', 'item_category_x', 'item_id_y', 'item_category_y']]

    return match_item_pair


def get_category_item_frequent(match_item_pair):
    # 统计各个类别总的出现次数
    item_category = pd.concat([match_item_pair['item_category_x'], match_item_pair['item_category_y']],
                              ignore_index=True)
    item_category_count = item_category.value_counts()
    item_category_count = item_category_count.to_dict()

    return item_category_count


def get_sorted_category(match_item_pair):
    match_category = match_item_pair[['item_category_x', 'item_category_y']]

    # 匹配是相互的，AB 与 BA 是等价的概念，故对AB与BA进行合并
    gap_bool = match_category['item_category_x'] < match_category['item_category_y']
    match_category_a = match_category[gap_bool]
    match_category_b = match_category[gap_bool == False]
    match_category_b.columns = ['item_category_y', 'item_category_x']
    match_category = pd.concat([match_category_a, match_category_b], ignore_index=True)

    return match_category


def calc_match_rate(match_item_pair, category_frequent):
    # match_rate = (a intersection b) / (a union b)
    match_category = get_sorted_category(match_item_pair)

    match_category_group = match_category.groupby(['item_category_x', 'item_category_y'])

    d = {}
    for key, group in match_category_group:
        rate = len(group) / (category_frequent[key[0]] + category_frequent[key[1]] - len(group))
        d[key] = [key[0], key[1], rate]

    d = pd.DataFrame.from_dict(d, orient='index')
    d.columns = ['item_category_x', 'item_category_y', 'category_match_rate']
    d = d.sort_values('category_match_rate', ascending=False)

    d['category_match_rate'] = d['category_match_rate'].map(lambda x: '%.8f' % x)
    print(d)

    return d


def main():
    # 读取匹配对
    match_item_pair = pd.read_csv(file_dim_fashion_matchsets)
    # 添加类别
    match_item_pair = add_item_category(match_item_pair)

    # 获取匹配对中各个类别出现的频率
    category_frequent = get_category_item_frequent(match_item_pair)

    # 计算匹配率
    d = calc_match_rate(match_item_pair, category_frequent)
    d.to_csv(file_ft_category_match_rate_by_match, index=False)


if __name__ == '__main__':
    main()
