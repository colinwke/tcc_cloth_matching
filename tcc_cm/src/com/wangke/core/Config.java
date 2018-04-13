package com.wangke.core;

/**
 * Created by colin on 2017/3/22.
 */
public class Config {
    public static final String FOLDER_CORE = "F:\\wk\\work\\tcc\\cm\\";

    public static final String BOUGHT_HISTORY = FOLDER_CORE + "user_bought_history.csv";

    // 数据划分
    public static final String FOLDER_DATA_SPLIT = FOLDER_CORE + "data_split\\";

    // 未对商品描述进行排序的数据
    public static final String ITEM_INFO = FOLDER_CORE + "dim_items.csv";
    public static final String OFFLINE_TRAIN_ITEM_INFO = FOLDER_DATA_SPLIT + "offline_train_info.csv";
    public static final String OFFLINE_TEST_ITEM_INFO = FOLDER_DATA_SPLIT + "offline_test_info.csv";
    public static final String ONLINE_TEST_ITEM_INFO = FOLDER_DATA_SPLIT + "online_test_info.csv";

    // 对商品描述进行排序后的数据
    public static final String ITEM_INFO_SORTED = FOLDER_CORE + "dim_items_sort.csv";
    public static final String OFFLINE_TRAIN_ITEM_INFO_SORTED = FOLDER_DATA_SPLIT + "offline_train_info_sorted.csv";
    public static final String OFFLINE_TEST_ITEM_INFO_SORTED = FOLDER_DATA_SPLIT + "offline_test_info_sorted.csv";
    public static final String ONLINE_TEST_ITEM_INFO_SORTED = FOLDER_DATA_SPLIT + "online_test_info_sorted.csv";

    // 生成的特征
    public static final String FOLDER_FEATURE = FOLDER_CORE + "feature\\";

    // 前面相似的商品个数
    public static final String OFFLINE_TRAIN_FRONT_WORD_COUNT = FOLDER_FEATURE + "offline_train_front_word_count.csv";
    public static final String OFFLINE_TEST_FRONT_WORD_COUNT = FOLDER_FEATURE + "offline_test_front_word_count.csv";
    public static final String ONLINE_TEST_FRONT_WORD_COUNT = FOLDER_FEATURE + "online_test_front_word_count.csv";

    // 前面相似商品的个数及相似词
    public static final String OFFLINE_TRAIN_FRONT_WORD = FOLDER_FEATURE + "offline_train_front_word.csv";
    public static final String OFFLINE_TEST_FRONT_WORD = FOLDER_FEATURE + "offline_test_front_word.csv";
    public static final String ONLINE_TEST_FRONT_WORD = FOLDER_FEATURE + "online_test_front_word.csv";

    // 相同的词语个数及相似词
    public static final String OFFLINE_TRAIN_SAME_WORD = FOLDER_FEATURE + "offline_train_same_word.csv";
    public static final String OFFLINE_TEST_SAME_WORD = FOLDER_FEATURE + "offline_test_same_word.csv";
    public static final String ONLINE_TEST_SAME_WORD = FOLDER_FEATURE + "online_test_same_word.csv";


    /**
     * 购买的历史记录
     */
    public static final String FILE_USER_BOUGHT_HISTORY = FOLDER_CORE + "user_bought_history_df_test_item_labeled.csv";
}
