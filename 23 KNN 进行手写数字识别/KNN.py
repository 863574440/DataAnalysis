from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC, LinearSVC
from sklearn.naive_bayes import MultinomialNB


def standard_scaler(train_x, test_x, train_y, test_y):
    ss = StandardScaler()
    train_x = ss.fit_transform(train_x)
    test_x = ss.transform(test_x)

    return train_x, test_x, train_y, test_y


def min_max_scaler(train_x, test_x, train_y, test_y):
    mms = MinMaxScaler()
    train_x = mms.fit_transform(train_x)
    test_x = mms.transform(test_x)

    return train_x, test_x, train_y, test_y


def processing_data():
    digits = load_digits()
    data = digits.data
    target = digits.target

    train_x, test_x, train_y, test_y = train_test_split(data, target, test_size=0.25)
    print(train_x.shape)
    print(test_x.shape)
    print(train_y.shape)
    print(test_y.shape)
    print("-" * 50)

    return train_x, test_x, train_y, test_y


def knn_model(train_x, test_x, train_y, test_y):
    # 使用 Z-Score 规范化数据， 保证每个维度的数据均值为 0，方差为 1
    train_x, test_x, train_y, test_y = standard_scaler(train_x, test_x, train_y, test_y)

    model = KNeighborsClassifier()
    model.fit(train_x, train_y)

    score = model.score(test_x, test_y)
    print("KNN score:", score)


def svc_model(train_x, test_x, train_y, test_y):
    # 使用 Z-Score 规范化数据， 保证每个维度的数据均值为 0，方差为 1
    train_x, test_x, train_y, test_y = standard_scaler(train_x, test_x, train_y, test_y)

    svc = SVC()
    svc.fit(train_x, train_y)
    score = svc.score(test_x, test_y)
    print("SVC socre:", score)


def linear_svc_moder(train_x, test_x, train_y, test_y):
    # 使用 Z-Score 规范化数据， 保证每个维度的数据均值为 0，方差为 1
    train_x, test_x, train_y, test_y = standard_scaler(train_x, test_x, train_y, test_y)

    linear_svc = LinearSVC()
    linear_svc.fit(train_x, train_y)
    score = linear_svc.score(test_x, test_y)
    print("LinearSVC socre:", score)


def native_bayes_model(train_x, test_x, train_y, test_y):
    train_x, test_x, train_y, test_y = min_max_scaler(train_x, test_x, train_y, test_y)

    model = MultinomialNB()
    model.fit(train_x, train_y)

    score = model.score(test_x, test_y)
    print("MultinomialNB socre:", score)


def main():
    train_x, test_x, train_y, test_y = processing_data()
    knn_model(train_x, test_x, train_y, test_y)
    svc_model(train_x, test_x, train_y, test_y)
    linear_svc_moder(train_x, test_x, train_y, test_y)
    native_bayes_model(train_x, test_x, train_y, test_y)


if __name__ == '__main__':
    main()
