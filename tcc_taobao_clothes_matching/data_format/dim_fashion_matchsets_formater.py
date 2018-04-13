"""
dim_fashion_matchsets 生成 match 对
"""
import itertools

import pandas as pd

from core.config import *


def drop_duplicates(df):
    divide_bool = df['item_id_x'] > df['item_id_y']
    left = df[divide_bool]
    right = df[divide_bool == False]
    right.columns = ['item_id_y', 'item_id_x']
    df = pd.concat([left, right], ignore_index=True)
    df = df.drop_duplicates()

    # values = df.values
    # for val in values:
    #     if val[0] > val[1]:
    #         val[0], val[1] = val[1], val[0]
    #
    # temp = pd.DataFrame(values)
    # temp = temp.drop_duplicates()

    return df


if __name__ == '__main__':
    # 读取txt 文件
    f = open(file_original_dim_fashion_matchsets)
    content = f.readlines()

    pieces_item_pairs = []
    for index, line in enumerate(content):
        index = index + 1
        # 读取一行数据
        line = line.replace('\n', '')
        # 去除标号
        line = line[(len(str(index)) + 1):]
        # 通过分号进行拆分
        sets = line.split(';')
        # 通过逗号进行拆分
        pieces = []
        for set in sets:
            pieces.append(set.split(','))

        for i1 in range(len(sets)):
            for i2 in range(i1 + 1, len(sets)):
                for i3 in itertools.product(pieces[i1], pieces[i2]):
                    pieces_item_pairs.append(i3)

    data = pd.DataFrame(pieces_item_pairs)
    data.columns = ['item_id_x', 'item_id_y']
    data = drop_duplicates(data)

    data.to_csv(file_dim_fashion_matchsets, index=False)
