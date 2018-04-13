"""
对dim_items.txt 进行格式化
原始格式
2632811 52 77003,154365,129681,64409,15463,117825,67630,116593,117719,94517,217074,31897,198337,17024,134130
格式化后
2632811,52,77003-154365-129681-64409-15463-117825-67630-116593-117719-94517-217074-31897-198337-17024-134130

并对商品描述的值进行排序

"""

import pandas as pd

from core.config import *


def format_depict(depict):
    depict = depict.split(',')
    # depict.sort(key=int)
    depict = '-'.join(depict)

    return depict


if __name__ == '__main__':
    f = open(file_original_dim_items)
    content = f.readlines()

    pieces = []
    for line in content:
        line = line.replace('\n', '')
        ele = line.split(' ')
        ele[2] = format_depict(ele[2])
        pieces.append(ele)

    data = pd.DataFrame(pieces)
    data.columns = ['item_id', 'item_category', 'item_depict']

    data.to_csv(file_dim_items, index=False)
