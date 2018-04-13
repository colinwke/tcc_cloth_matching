"""
通过目标商品集对购买记录的商品进行打标
"""

import pandas as pd
from core.config import *

OBJECT_ITEM_SET = file_test_items


def main():
    bh = pd.read_csv(file_user_bought_history_df)
    ti = pd.read_csv(OBJECT_ITEM_SET)

    bh['label'] = bh['item_id'].isin(ti['item_id']) * 1

    bh.to_csv(file_user_bought_history_df_lb, index=False)


if __name__ == '__main__':
    main()
