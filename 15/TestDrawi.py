import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd


def use_plt_scatter():
    s = np.random.random(size=(2, 100))
    plt.scatter(s[0], s[1], marker="o")  # 画散点图
    plt.show()


def use_seaborn_scatter():
    data = np.random.random(size=(2, 1000))
    dataframe = pd.DataFrame({'x': data[0], 'y': data[1]})
    sns.jointplot(x='x', y='y', data=dataframe, kind='scatter')  # 画散点图
    plt.show()


def use_plt_zhexian():
    x = np.arange(2000, 2020, step=1, dtype=np.int32)
    y = np.random.randint(20, 100, size=(20,))
    plt.plot(x, y)  # 画折线图
    plt.show()
    print(len(y))


def zhexian_use_seaborn():
    x = np.arange(2000, 2020, step=1, dtype=np.int32)
    y = np.random.randint(20, 100, size=(20,))
    dataframe = pd.DataFrame({"x": x, "y": y})
    sns.lineplot(x="x", y="y", data=dataframe)
    plt.show()


if __name__ == '__main__':
    # use_plt_scatter()
    # use_seaborn_scatter()
    # use_plt_zhexian()
    zhexian_use_seaborn()
