import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn import svm, metrics


def process_data():
    data = pd.read_csv("./data/data.csv")
    # 将特征字段分为三组
    features_mean = list(data.columns[2:12])
    features_se = list(data.columns[12:22])
    features_worst = list(data.columns[22:32])

    data.drop("id", axis=1, inplace=True)
    data["diagnosis"] = data["diagnosis"].map({'M': 1, 'B': 0})
    sns.countplot(data["diagnosis"], label="count")
    plt.show()

    corr = data[features_mean].corr()  # 计算各个变量之间的相关性 corr()
    plt.figure(figsize=(14, 14))
    sns.heatmap(corr, annot=True)  # 画出热力图, annot=True 显示每个方格的数据
    plt.show()

    # 特征选择
    features_remain = ['radius_mean', 'texture_mean', 'smoothness_mean', 'compactness_mean', 'symmetry_mean',
                       'fractal_dimension_mean']

    train, test = train_test_split(data, test_size=0.3)
    train_x = train[features_remain]
    train_y = train["diagnosis"]
    test_x = test[features_remain]
    test_y = test["diagnosis"]

    # 使用 Z-Score 规范化数据， 保证每个维度的数据均值为 0，方差为 1
    ss = StandardScaler()
    train_x = ss.fit_transform(train_x)
    test_x = ss.transform(test_x)

    return train_x, train_y, test_x, test_y


def train_model(train_x, train_y):
    # 创建 SVM 分类器
    model = svm.SVC()
    model.fit(train_x, train_y)
    return model


def predict_test(model, test_x, test_y):
    predicted_y = model.predict(test_x)
    score = metrics.accuracy_score(predicted_y, test_y)
    print(score)


def main():
    train_x, train_y, test_x, test_y = process_data()
    model = train_model(train_x, train_y)
    predict_test(model, test_x, test_y)


if __name__ == '__main__':
    main()
