"""
测试商品一共有5462个商品，但是在购买记录中只有2768个
因此需要对没有出现在购买记录的测试商品进行替换
"""

import pandas as pd

from core.config import *


def get_similarity_rate(s1, s2):
    return len(s1 & s2)


def get_black_item_map(black_item, item_info, bought_history_item):
    d = {}
    black_item_group = black_item.groupby('item_category')
    for category, group in black_item_group:
        # 1. 同类
        similarity_item_bak = item_info[item_info['item_category'] == category]
        for val in group.values:
            # 2. 最相似
            similarity_rate = similarity_item_bak['item_depict'].map(lambda x: get_similarity_rate(val[2], x))
            similarity_item = pd.concat([similarity_item_bak, similarity_rate], axis=1, ignore_index=True)
            similarity_item.columns = ['item_id', 'item_category', 'item_depict', 'rate']
            similarity_item = similarity_item[['item_id', 'rate']]
            # 3. 出现在购买记录中
            similarity_item = similarity_item[similarity_item['item_id'].isin(bought_history_item)]
            similarity_item = similarity_item.sort_values('rate')
            d[val[0]] = [val[0], int(similarity_item.iloc[0, 0])]

    return d


def main():
    # 1. 得到没有出现在购买记录中的测试商品集合
    # 2. 在同类中找到最为相似的1个商品，且出购买记录中有出现
    # 3. 生成映射
    bought_history = pd.read_csv(file_user_bought_history)
    bought_history_item = bought_history['item_id'].drop_duplicates()
    item_info = pd.read_csv(file_dim_items)
    item_info['item_depict'] = item_info['item_depict'].map(lambda x: set(x.split('-')))
    test_item = pd.read_csv(file_test_items)

    # 找到没有出现在购买记录中的测试商品
    black_item = test_item[test_item['item_id'].isin(bought_history_item) == False]

    # print(black_item)
    # black_item.to_csv(folder_core + 'item_test')
    # exit(3)

    # 为test_item添加类别
    black_item = pd.merge(black_item, item_info, how='left', on='item_id')[['item_id', 'item_category', 'item_depict']]

    # 寻找每个black_item的替代商品
    black_item_map = get_black_item_map(black_item, item_info, bought_history_item)
    black_item_map = pd.DataFrame.from_dict(black_item_map, orient='index')
    black_item_map.columns = ['black_item', 'replace_item']

    black_item_map.to_csv(folder_core + 'black_test_item_map.csv', index=False)


if __name__ == '__main__':
    main()
