import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.feature_extraction import DictVectorizer
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import AdaBoostClassifier


def get_data():
    train_data = pd.read_csv("./data/train.csv")  # 891个样本， 每个样本12个特征
    test_data = pd.read_csv("./data/test.csv")  # 481个样本， 每个样本11个特征，缺少是否存活
    return train_data, test_data


def predict(train_data, test_data):
    print('tarin_data shape:', train_data.shape)
    print('test_data shape:', test_data.shape)
    print("-" * 30)
    print("train data info:")
    print(train_data.info())
    print("-" * 30, "\n")
    print("train data descirbe:")
    print(train_data.describe())
    print("-" * 30)
    print(train_data["Embarked"].value_counts())

    print(test_data.info())

    # 清洗数据
    # 使用平均年龄填充缺失值
    train_data["Age"].fillna(train_data["Age"].mean(), inplace=True)
    test_data["Age"].fillna(test_data["Age"].mean(), inplace=True)
    # 使用平均价格填充缺失值
    train_data["Fare"].fillna(train_data["Fare"].mean(), inplace=True)
    test_data["Fare"].fillna(test_data["Fare"].mean(), inplace=True)
    # 使用登陆最多的港口填充缺失值
    train_data["Embarked"].fillna("S", inplace=True)
    test_data["Embarked"].fillna("S", inplace=True)

    # 特征选择
    features = ["Pclass", "Sex", "Age", "SibSp", "Parch", "Fare", "Embarked"]
    train_features = train_data[features]
    train_labels = train_data["Survived"]
    test_features = test_data[features]

    dvec = DictVectorizer(sparse=False)
    train_features = dvec.fit_transform(train_features.to_dict(orient='record'))
    feature_names = dvec.feature_names_
    print(train_features)
    print(feature_names)
    print(train_features.shape)

    # 弱分类器
    base_clf = DecisionTreeClassifier(max_depth=1, min_samples_leaf=1)
    base_clf.fit(train_features, train_labels)
    k_score = cross_val_score(base_clf, train_features, train_labels, cv=10)
    print("base_clf k折准确率：", k_score.mean())

    # 决策树分类器
    clf = DecisionTreeClassifier(criterion="entropy")
    clf.fit(train_features, train_labels)
    k_score = cross_val_score(clf, train_features, train_labels, cv=10)
    print("clf k折准确率：", k_score.mean())

    # adaboost 分类器
    ada = AdaBoostClassifier()
    ada.fit(train_features, train_labels)
    k_score = cross_val_score(ada, train_features, train_labels, cv=10)
    print("ada k折准确率：", k_score.mean())


def main():
    train_data, test_data = get_data()
    predict(train_data, test_data)


if __name__ == '__main__':
    main()
