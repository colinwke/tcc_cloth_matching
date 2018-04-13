"""
对用户购买记录的文件进行格式化
"""

import pandas as pd

from core.config import *

if __name__ == '__main__':
    data = pd.read_csv(file_original_test_items, header=None)
    data.columns = ['item_id']

    data.to_csv(file_test_items, index=False)
