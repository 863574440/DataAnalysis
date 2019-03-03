import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.mixture import GaussianMixture
from sklearn.metrics import calinski_harabaz_score


def load_data(heros):
    features = ['最大生命', '生命成长', '初始生命', '最大法力', '法力成长', '初始法力', '最高物攻', '物攻成长', '初始物攻',
                '最大物防', '物防成长', '初始物防', '最大每5秒回血', '每5秒回血成长', '初始每5秒回血', '最大每5秒回蓝',
                '每5秒回蓝成长', '初始每5秒回蓝', '最大攻速', '攻击范围']
    data = heros[features]

    # 设置 plt 正确显示中文
    # plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
    # plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
    # corr = data.corr()
    # plt.figure(figsize=(14, 14))
    # sns.heatmap(corr, annot=True)
    # plt.show()

    data["最大攻速"] = data["最大攻速"].apply(lambda x: float(x.strip('%')) / 100)
    data["攻击范围"] = data["攻击范围"].map({"远程": 1, "近战": 0})

    ss = StandardScaler()
    ss.fit_transform(data)

    return data


def train_model(data):
    gmm = GaussianMixture(n_components=30, covariance_type='full')
    gmm.fit(data)
    # 训练数据
    prediction = gmm.predict(data)
    return prediction


def main():
    heros = pd.read_csv("./data/heros.csv", encoding="ANSI")
    data = load_data(heros)
    prediction = train_model(data)
    print(prediction)
    heros.insert(0, "分组", prediction)
    heros.to_csv("result.csv", index=False)

    print(calinski_harabaz_score(data, prediction))


if __name__ == '__main__':
    main()
