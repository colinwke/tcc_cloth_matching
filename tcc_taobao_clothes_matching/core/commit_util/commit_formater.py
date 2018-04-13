"""
根据front_same_count_test_items.csv生成提交文件
"""
import pandas as pd

from core.result_commit import commit_online
from core.result_commit import evaluate

# IS_OFFLINE = True
IS_OFFLINE = False


def main():
    # data = pd.read_csv(folder_core + 'front_word_count_reverse.csv')
    # data = pd.read_csv(r"F:\wk\work\tcc\cm\feature\online_test_front_word_count_f.csv")
    # data = pd.read_csv(r'F:\wk\work\tcc\cm\user_bought_history_match_day365_f.csv')
    data = pd.read_csv(r'F:\wk\work\tcc\cm\v4\feature\bought_history\user_bought_history_match_day365.csv')
    data = data[['item_id_x', 'item_id_y']]

    d = {}
    for val in data.values:
        if val[0] in d:
            if len(d[val[0]]) <= 200:
                d[val[0]].append(val[1])
        else:
            d[val[0]] = [val[1]]  # d[val[0]] = []

    if IS_OFFLINE:
        evaluate(d)
    else:
        commit_online(d)


if __name__ == '__main__':
    main()
