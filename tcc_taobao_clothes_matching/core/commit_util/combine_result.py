"""
两个答案的融合

读取两个答案文件
如果答案A长度小于200
则使用答案B进行补充
"""

from core.result_commit import save_commit

folder = r'F:\wk\work\tcc\cm\commit\2017-3-28temp\fm_submissions_'

files = [
    folder + 'fw.csv',
    # folder + 'd1.csv',
    # folder + 'd7.csv',
    # folder + 'd365.csv'
    folder + '20.csv'
]


def dict_file(file_name):
    f = open(file_name, 'r')
    content = f.readlines()

    d = {}
    for line in content:
        line = line.replace('\n', '')
        ele = line.split(' ')
        d[ele[0]] = ele[1].split(',')

    f.close()

    return d


def combine(ra, rb):
    for key in ra:
        if (len(ra[key]) < 200) & (key in rb):
            ra[key] = ra[key] + [i for i in rb[key][:200] if i not in ra[key]]

    for key in rb:
        if key not in ra:
            ra[key] = rb[key]

    return ra


def main():
    # 读取数据
    pieces = []
    for file in files:
        pieces.append(dict_file(file))

    # 进行合并
    ra = pieces[0]
    for i, piece in enumerate(pieces):
        if i == 0:
            continue
        ra = combine(ra, piece)

    save_commit(ra)


if __name__ == '__main__':
    main()
