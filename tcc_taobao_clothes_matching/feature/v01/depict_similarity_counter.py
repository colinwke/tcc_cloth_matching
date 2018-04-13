"""
商品的描述相似度进行配对
1. 对测试商品进行分类
2. 获取与该类别能配对的类别
3. 逐一计算相似度
4. 相似度进行排序
5. 结果生成

对rule01 进行性能更改
"""

import pandas as pd

from core.config import *

from feature.v01.match_category_list_generator import *

# ============================================
# IS_OFFLINE = True
IS_OFFLINE = False

# 取相似度>0商品的最大个数
VALID_COUNT = 1 * 1000
# 类别之间匹配率最高的前a%个类别对
THRESHOLD_MATCH_LIST = 0.2

# 评价模式
PARAMS_COMMIT = True


# PARAMS_COMMIT = False


# ============================================
# ============================================

def get_test_item(item_all):
    if IS_OFFLINE:
        data = pd.read_csv(file_offline_train_item)
    else:
        data = pd.read_csv(file_test_items)
    # 添加类别及描述信息
    data = pd.merge(data, item_all, how='left', on='item_id')

    return data


def get_category_item(item):
    dict_cate = {}

    for val in item.values:
        if val[1] not in dict_cate:
            dict_cate[val[1]] = []
        dict_cate[val[1]].append(val[0])

    return dict_cate


def calc_similarity(t1, t2):
    return len((t1 & t2))  # / (len(t1) + len(t2))


def get_similar_df(val, item_b):
    similarity_val = item_b['item_depict'].map(lambda x: calc_similarity(x, val[2]))
    temp = pd.concat([item_b.drop(['item_category', 'item_depict'], axis=1), similarity_val],
                     axis=1, ignore_index=True)
    temp.columns = ['item_id', 'value']
    item_match_result = temp[temp['value'] > 0].sort_values('value', ascending=False)

    if len(item_match_result) > VALID_COUNT:
        item_match_result = item_match_result[:VALID_COUNT]

    item_match_result['item_id_x'] = [val[0]] * len(item_match_result)

    return item_match_result


def main():
    # 读取所有商品的信息
    item_all = pd.read_csv(file_dim_items)
    item_all['item_depict'] = item_all['item_depict'].map(lambda x: set(map(int, x.split('-'))))
    # 读取测试集
    item_test = get_test_item(item_all)
    # item_test = item_test[:3]

    # 读取类别匹配列表
    dict_category_match_list = generate_match_list_by_all(THRESHOLD_MATCH_LIST)

    # 对测试数据集进行分类
    dict_category_test = get_category_item(item_test)

    # 进行计算
    pieces = []
    for cate_key in dict_category_test:
        # 通过与cate_key 相匹配的类别过滤匹配商品
        item_a = item_test[item_test['item_id'].isin(dict_category_test[cate_key])]
        print('test item count:', len(item_a))
        item_b = item_all[item_all['item_category'].isin(dict_category_match_list[cate_key])]
        print('may match cate count:', len(dict_category_match_list[cate_key]), '/ item count:', len(item_b))

        for val in item_a.values:
            pieces.append(get_similar_df(val, item_b))

    pieces = pd.concat(pieces, ignore_index=True)
    pieces.columns = ['item_id_y', 'value', 'item_id_x']
    pieces = pieces[['item_id_x', 'item_id_y', 'value']]

    pieces.to_csv(file_ft_test_similar_count, index=False)


if __name__ == '__main__':
    main()
