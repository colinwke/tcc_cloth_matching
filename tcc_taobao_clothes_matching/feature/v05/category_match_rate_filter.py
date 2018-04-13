"""
通过类别比例过滤匹配对
"""

import pandas as pd

from core.config import *

file_item_pair = ''
pass_rate = 0.4


def get_full_category_match_pair_rate(category_match_pair_rate):
    """
    因为类别匹配对是唯一对，需要对匹配对的两种情况进行考虑
    对原始的匹配对进行逆转复制
    """
    category_match_pair_rate_reverse = category_match_pair_rate[
        ['item_category_y', 'item_category_x', 'category_match_rate']]
    category_match_pair_rate_reverse.columns = category_match_pair_rate.columns
    category_match_pair_rate = pd.concat([category_match_pair_rate, category_match_pair_rate_reverse],
                                         ignore_index=True)

    return category_match_pair_rate


def get_pass_line(category_match_pair_rate):
    pass_line = {}
    for val in category_match_pair_rate.values:
        if val[0] not in pass_line:
            pass_line[val[0]] = []
        pass_line[val[0]].append(val[2])

    # 及格线
    for key in pass_line:
        pass_line[key] = pass_line[key][int(len(pass_line[key]) * pass_rate)]

    return pass_line


def add_item_category(data, category_match_pair_rate):
    # 添加类别
    item_info = pd.read_csv(file_dim_items)
    item_info = item_info[['item_id', 'item_category']]

    data = pd.merge(data, item_info, how='left', left_on='item_id_x', right_on='item_id')
    data = pd.merge(data, item_info, how='left', left_on='item_id_y', right_on='item_id')
    data = data.iloc[:, [0, 1, 2, 4, 6]]

    # 添加类别匹配率
    data = pd.merge(data, category_match_pair_rate, how='left', left_on=['item_category_x', 'item_category_y'],
                    right_on=['item_category_x', 'item_category_y'])

    return data


def main():
    data = pd.read_csv(file_item_pair)

    category_match_pair_rate = pd.read_csv(file_ft_category_match_rate_by_all)

    # 获取类别匹配值及格线
    dict_pass_line = get_pass_line(category_match_pair_rate)

    data = add_item_category(data, category_match_pair_rate)

    # 删除没有类别匹配的匹配对
    data = data.dropna(axis=0)
    # 添加及格线
    data['rate_pass_line'] = data['item_category_x'].map(dict_pass_line)
    # 过滤
    data = data[data['category_match_rate'] > data['rate_pass_line']]

    # 保存
    file_save = file_item_pair.split('.')
    data[[0, 1, 2]].to_csv(file_save[0] + '_filter.csv', index=False)


if __name__ == '__main__':
    main()
