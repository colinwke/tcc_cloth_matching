"""
对日期进行重编码
按照天数计算
"""

import pandas as pd
from core.config import *


def main():
    bh = pd.read_csv(file_user_bought_history)

    date = bh['date'].drop_duplicates().sort_values()
    date.index = range(len(date))
    date = date.reset_index()
    dv = date.values

    dd = dict((val[1], val[0]) for val in dv)

    bh['date'] = bh['date'].map(dd)
    bh.to_csv(file_user_bought_history_df, index=False)


if __name__ == '__main__':
    main()
