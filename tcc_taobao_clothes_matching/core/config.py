"""
文件路径配置
"""

folder_core = 'F:\\wk\\work\\tcc\\cm\\'

# 原始数据
folder_original = folder_core + 'original\\'
file_original_dim_fashion_matchsets = folder_original + 'dim_fashion_matchsets.txt'
file_original_dim_items = folder_original + 'dim_items.txt'
file_original_user_bought_history = folder_original + 'user_bought_history.txt'
file_original_test_items = folder_original + 'test_items.txt'

# 格式化后的数据
file_dim_fashion_matchsets = folder_core + 'dim_fashion_matchsets.csv'
file_dim_items = folder_core + 'dim_items.csv'
file_user_bought_history = folder_core + 'user_bought_history.csv'
file_test_items = folder_core + 'test_items.csv'

# 线下数据集
folder_item_set = folder_core + 'item_set\\'
file_offline_train_item = folder_item_set + 'offline_train_item.csv'
file_offline_test_item = folder_item_set + 'offline_test_item.csv'
# 验证数据
file_offline_reference_data_pickle = folder_core + "offline_reference_data.pickle"
# 线上提交路径
file_online_commit = folder_core + 'commit\\fm_submissions.csv'

# 特征
folder_feature = folder_core + 'feature\\'
# 类别匹配率
file_ft_category_match_rate_by_all = folder_feature + 'category_match_rate_by_all.csv'
file_ft_category_match_rate_by_match = folder_feature + 'category_match_rate_by_match.csv'
# 测试集商品相似个数计算
file_ft_test_similar_count = folder_feature + 'test_item_similar_count.csv'


# 通过用户的购买记录进行统计
# 日期重编码
file_user_bought_history_df = folder_core + 'user_bought_history_df.csv'
# 通过是否在目标集进行标记
file_user_bought_history_df_lb = folder_core + 'file_user_bought_history_df_lb.csv'



































#
# # 生成数据
# file_category_match_pair = folder_core + 'category_match_pair.csv'
# file_category_match_list = folder_core + 'category_match_list.pickle'
#
# # 验证集数据
# file_offline_reference_item_set = folder_core + 'offline_reference_item_set.pickle'
# file_offline_reference_item_data = folder_core + 'offline_reference_item_data.pickle'
#
# # 提交结果
# file_online_commit = folder_core + 'commit\\fm_submissions.csv'
# file_online_commit_pickle = folder_core + 'commit\\fm_submissions.pickle'
#
# # 特征
# folder_feature = folder_core + 'feature\\'
# # 类别与类别之间的匹配比率
# file_ft_gp_c1_c2_match_rate = folder_feature + 'gp_c1_c2_match_rate.csv'
# # 单一类别商品总数与匹配总数比率
# file_ft_gp_c_match_rate = folder_feature + 'gp_c_match_rate.csv'
#
# 线下训练及线下验证商品生成
# file_offline_train_item = folder_core + 'offline_train_item.csv'
# file_offline_test_item = folder_core + 'offline_test_item.csv'
