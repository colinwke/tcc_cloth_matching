"""
快速保存及加载pickle数据
"""

import pickle


def load_pickle(file_name):
    with open(file_name, 'rb') as f:
        return pickle.load(f)


def dump_pickle(data, file_name):
    with open(file_name, 'wb') as f:
        pickle.dump(data, f, pickle.HIGHEST_PROTOCOL)
