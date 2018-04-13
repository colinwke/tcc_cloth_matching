"""
计算类别之间的匹配率
数据来源于已经匹配好的商品
计算公式：match_rate = (a intersection b) / (a union b)
"""

import pandas as pd

from core.config import *


def add_item_category(match_item_pair, item_info):
    match_item_pair = pd.merge(match_item_pair, item_info, how='left', left_on='item_id_x', right_on='item_id')
    match_item_pair = pd.merge(match_item_pair, item_info, how='left', left_on='item_id_y', right_on='item_id')
    match_item_pair = match_item_pair[['item_id_x', 'item_category_x', 'item_id_y', 'item_category_y']]

    return match_item_pair


def get_category_item_frequent(item_info):
    # 统计各个类别总的商品个数
    item_category = item_info['item_category']
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
    """
    对于类别A
    于类别B匹配商品的个数 / 类别B总的商品个数
    """
    match_category = get_sorted_category(match_item_pair)
    match_category_group = match_category.groupby(['item_category_x', 'item_category_y'])

    d = {}
    for key, group in match_category_group:
        d[key] = [key[0], key[1], len(group) / category_frequent[key[1]]]
        d[(key[1], key[0])] = [key[1], key[0], len(group) / category_frequent[key[0]]]

    d = pd.DataFrame.from_dict(d, orient='index')
    d.columns = ['item_category_x', 'item_category_y', 'category_match_rate']
    d = d.sort_values('category_match_rate', ascending=False)

    d['category_match_rate'] = d['category_match_rate'].map(lambda x: '%.8f' % x)
    print(d)

    return d


def main():
    # 读取匹配对
    match_item_pair = pd.read_csv(file_dim_fashion_matchsets)
    # 读取所有商品
    item_info = pd.read_csv(file_dim_items)
    # 添加类别
    match_item_pair = add_item_category(match_item_pair, item_info)

    # 获取匹配对中各个类别出现的频率
    category_frequent = get_category_item_frequent(item_info)

    # 计算匹配率
    d = calc_match_rate(match_item_pair, category_frequent)
    d.to_csv(file_ft_category_match_rate_by_all, index=False)


if __name__ == '__main__':
    main()
