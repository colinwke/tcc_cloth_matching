"""
1. 测试商品集随时间购买次数
2. 匹配商品集随时间购买次数

通过1,2的图像可得，测试商品集是从匹配商品集中抽样出来的
因此可直接从匹配商品集合中抽样出线下训练和测试商品集

生成训练集和验证集
训练集5500
验证集2541
"""

import pandas as pd
import matplotlib.pyplot as plt

from core.config import *


def plot_itemset_bought_count2(itemset, history, multi_factor=1):
    history = history[history['item_id'].isin(itemset)]
    plot_itemset_bought_count(history, multi_factor)


def plot_itemset_bought_count(history, multi_factor=1):
    bought_count = history['date'].value_counts()
    if multi_factor is not 1:
        bought_count *= multi_factor

    bought_count = bought_count.sort_index()
    bought_count.plot()


def simple_sample(match_set, frac=0.08):
    match_set = match_set.sample(frac=frac)
    print(len(match_set))

    return match_set


def sample_set(match_set):
    """
    抽样方法1：
    先抽取6000个商品
    再抽取5000个作为训练商品，1000个作为测试商品
    """
    match_set = simple_sample(match_set, 0.132)  # frac=0.132 -> 8041个样本
    # 前面5000做训练集
    # 后面1500做测试集
    gap = 5500
    train_set = match_set[:gap]
    test_set = match_set[gap:]

    train_set1 = pd.DataFrame(train_set)
    train_set1.columns = ['item_id']
    test_set1 = pd.DataFrame(test_set)
    test_set1.columns = ['item_id']

    train_set1.to_csv(file_offline_train_item, index=False)
    test_set1.to_csv(file_offline_test_item, index=False)

    return train_set, test_set


def main():
    history = pd.read_csv(file_user_bought_history)
    history['date'] = history['date'].map(str)

    match_set = pd.read_csv(file_dim_fashion_matchsets)
    match_set = pd.concat([match_set['item_id_x'], match_set['item_id_y']], ignore_index=True)
    match_set = match_set.drop_duplicates()

    test_set = pd.read_csv(file_test_items)
    test_set = test_set['item_id']

    train_set, test_set2 = sample_set(match_set)

    plot_itemset_bought_count2(test_set, history)
    plot_itemset_bought_count2(train_set, history)
    plot_itemset_bought_count2(test_set2, history, multi_factor=2.5)
    plt.show()


if __name__ == '__main__':
    main()
