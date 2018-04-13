"""
对用户购买记录的文件进行格式化
"""

import pandas as pd

from core.config import *

if __name__ == '__main__':
    data = pd.read_csv(file_original_user_bought_history, sep=' ', header=None)
    data.columns = ['user_id', 'item_id', 'date']

    data.to_csv(file_user_bought_history, index=False)
