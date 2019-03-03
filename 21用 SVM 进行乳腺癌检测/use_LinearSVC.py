import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn import svm, metrics


def processes_data():
    data = pd.read_csv("./data/data.csv")
    data.drop("id", axis=1, inplace=True)
    data["diagnosis"] = data["diagnosis"].map({"M": 1, "B": 0})

    features = list(data.columns[1:])

    train, test = train_test_split(data, test_size=0.3)
    train_x = train[features]
    train_y = train["diagnosis"]
    test_x = test[features]
    test_y = test["diagnosis"]

    # 使用 Z-Score 规范化数据， 保证每个维度的数据均值为 0，方差为 1
    ss = StandardScaler()
    train_x = ss.fit_transform(train_x)
    test_x = ss.transform(test_x)

    return train_x, train_y, test_x, test_y


def train_model(train_x, train_y):
    model = svm.LinearSVC()
    model.fit(train_x, train_y)
    return model


def predict_test(model, test_x, test_y):
    predicted_y = model.predict(test_x)
    score = metrics.accuracy_score(predicted_y, test_y)
    print(score)


def main():
    train_x, train_y, test_x, test_y = processes_data()
    model = train_model(train_x, train_y)
    predict_test(model, test_x, test_y)


if __name__ == '__main__':
    main()
