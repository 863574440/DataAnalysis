import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.feature_extraction import DictVectorizer
from sklearn.model_selection import cross_val_score
import graphviz
from sklearn.tree import export_graphviz


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

    clf = DecisionTreeClassifier(criterion="entropy")
    clf.fit(train_features, train_labels)

    test_features = dvec.transform(test_features.to_dict(orient='record'))
    pre_labels = clf.predict(test_features)
    print(pre_labels)

    # 得到决策树准确率
    acc_decision_tree = clf.score(train_features, train_labels)
    print(u'score 准确率为 %.4lf' % acc_decision_tree)

    # 使用k折计算模型准确率
    k_score = cross_val_score(clf, train_features, train_labels, cv=10)
    print(k_score)
    print("k折准确率：", k_score.mean())
    return clf, feature_names


def draw_tree(tree_model, feature_names):
    dot_data = export_graphviz(tree_model,
                               out_file=None,
                               feature_names=feature_names)
    graph = graphviz.Source(dot_data)
    graph.render("Titanic", "./data/", view=True)


def main():
    train_data, test_data = get_data()
    clf, feature_names = predict(train_data, test_data)
    draw_tree(clf, feature_names)


if __name__ == '__main__':
    main()
