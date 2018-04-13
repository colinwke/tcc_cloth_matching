# coding: utf-8
import pandas as pd
item_info = pd.read_csv('dim_items.csv')
item_info.head()
offline_test = pd.read_csv('offline_test_item.csv')
offline_test
offline_train = pd.read_csv('offline_train_item.csv')
online_test = pd.read_csv('test_items.csv')
online_test_info = item_info[item_info['item_id'].isin(online_test['item_id'])]
online_test_info.head()
online_test_info.to_csv('online_test_info.csv', index=False)
offline_test_info = item_info[item_info['item_id'].isin(offline_test['item_id'])]
offline_test_info.to_csv('offline_test_info.csv', index=False)
offline_train_info = item_info[item_info['item_id'].isin(offline_train['item_id'])]
offline_train_info.to_csv('offline_train_info.csv', index=False)
