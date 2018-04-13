"""
通过用户的购买记录进行匹配
1. 1天
2. 8天
3. 16天
"""

import pandas as pd
import itertools


def cut_block(bh):
    # 通过用户和时间划分数据
    d = {}  # {(user_id, date): [[test_item1, ...], [match_item1, ...]], ...}
    for val in bh.values:
        # val[user_id, item_id, date, label]
        if (val[0], val[2]) not in d:
            if val[3] == 1:
                # test_item
                d[(val[0], val[2])] = [[val[1]], []]
            else:
                d[(val[0], val[2])] = [[], [val[1]]]
        else:
            if val[3] == 1:
                # test_item
                d[(val[0], val[2])][0].append(val[1])
            else:
                d[(val[0], val[2])][1].append(val[1])

    return d


def count_pair(d):
    # 生成匹配对并统计数量
    d2 = {}  # {(test_item, match_item): count}
    for key in d:
        if (len(d[key][0]) != 0) & (len(d[key][1]) != 0):
            for test_match in itertools.product(d[key][0], d[key][1]):
                if test_match not in d2:
                    d2[test_match] = [test_match[0], test_match[1], 1]
                else:
                    d2[test_match][2] += 1

    return d2


def main():
    bh = pd.read_csv(r'F:\wk\work\tcc\cm\v3\user_bought_history_df_test_item_labeled.csv')
    # bh['date'] = bh['date'] % 7  # 以n天为一个单位进行统计

    d = cut_block(bh)
    print('stage 1 finished')

    d2 = count_pair(d)
    print('stage 2 finished')

    d2 = pd.DataFrame.from_dict(d2, orient='index')
    d2.columns = ['item_id_x', 'item_id_y', 'day1']
    d2 = d2.sort_values(['item_id_x', 'day1'], ascending=False)

    d2.to_csv(r'F:\wk\work\tcc\cm\user_bought_history_match_day1.csv', index=False)


if __name__ == '__main__':
    main()
