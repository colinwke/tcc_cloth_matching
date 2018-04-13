# coding: utf-8
import pandas as pd

item_info = pd.read_csv('dim_items_sorted.csv')

offline_test = pd.read_csv('offline_test_item.csv')
offline_train = pd.read_csv('offline_train_item.csv')
online_test = pd.read_csv('online_test_item.csv')

online_test_info = item_info[item_info['item_id'].isin(online_test['item_id'])]
online_test_info.to_csv('online_test_info_sorted.csv', index=False)
offline_test_info = item_info[item_info['item_id'].isin(offline_test['item_id'])]
offline_test_info.to_csv('offline_test_info_sorted.csv', index=False)
offline_train_info = item_info[item_info['item_id'].isin(offline_train['item_id'])]
offline_train_info.to_csv('offline_train_info_sorted.csv', index=False)
