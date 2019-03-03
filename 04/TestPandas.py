import pandas as pd


def test_series():
    x1 = pd.Series([1, 2, 3, 4], index=["a", "b", "c", "d"])
    print(x1)

    x2 = pd.Series({"hh": 3, "bb": "12"})
    print(x2)


def test_dataframe():
    data = {'Chinese': [66, 95, 93, 90, 80], 'English': [65, 85, 92, 88, 90], 'Math': [30, 98, 96, 77, 90]}
    df1 = pd.DataFrame(data)
    df2 = pd.DataFrame(data, index=['ZhangFei', 'GuanYu', 'ZhaoYun', 'HuangZhong', 'DianWei'],
                       columns=['English', 'Math', 'Chinese'])
    print(df1)
    print(df2)
    print()

    # # 导出文件
    # df2.to_csv("./data/xx.csv")
    # df2.to_excel("./data/xx.xlsx")
    # print()
    #
    # # 读取文件
    # score = pd.read_excel("./data/xx.xlsx")
    # print(score)
    # print(type(score))

    # print(df2.rename(columns={"Chinese": "yuwen"}, inplace=False))
    # print(df2)
    # print(df2["English"])  # 获取某一列

    print(df2.describe())
    ''' 输出
             English       Math    Chinese
    count   5.000000   5.000000   5.000000
    mean   84.000000  78.200000  84.800000
    std    10.931606  28.163807  11.987493
    min    65.000000  30.000000  66.000000
    25%    85.000000  77.000000  80.000000
    50%    88.000000  90.000000  90.000000
    75%    90.000000  96.000000  93.000000
    max    92.000000  98.000000  95.000000    
    '''


def exercise():
    # 1. 对于下表的数据，请使用Pandas中的DataFrame进行创建，并对数据进行清洗。
    # 2. 同时新增一列“总和”计算每个人的三科成绩之和。

    # 列名使用了中文，打印对其的话，需要设置这两个参数
    pd.set_option('display.unicode.ambiguous_as_wide', True)
    pd.set_option('display.unicode.east_asian_width', True)

    data = {"姓名": ["张飞", "关羽", "赵云", "黄忠", "典韦", "典韦"],
            "语文": [66, 95, 95, 90, 80, 80],
            "英语": [65, 85, 92, 88, 90, 90],
            "数学": [None, 98, 96, 77, 90, 90]}

    score_table = pd.DataFrame(data, columns=["姓名", "语文", "英语", "数学"])
    print(score_table, "\n")

    # 除去多余行
    score_table.drop_duplicates(inplace=True)
    print(score_table, "\n")

    # 添加 总分 列
    score_table.fillna(0, inplace=True)  # 将NaN替换为0
    score_table["总分"] = score_table["语文"] + score_table["英语"] + score_table["数学"]
    print(score_table)


def main():
    # test_series()
    # test_dataframe()
    exercise()


if __name__ == '__main__':
    main()
