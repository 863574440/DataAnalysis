import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

pd.set_option('display.unicode.ambiguous_as_wide', True)
pd.set_option('display.unicode.east_asian_width', True)


def processing_data():
    data = pd.read_csv("./data/data.csv", encoding="gbk")
    train_x = data[["2019年国际排名", "2018世界杯", "2015亚洲杯"]]
    ss = StandardScaler()
    train_x = ss.fit_transform(train_x)
    return data, train_x


def train_model(train_x):
    kmeans = KMeans(n_clusters=5)
    kmeans.fit(train_x)
    predict_y = kmeans.predict(train_x)
    return predict_y


def main():
    data, train_x = processing_data()
    predict_y = train_model(train_x)
    result = pd.concat((data, pd.DataFrame(predict_y)), axis=1)
    result.rename(columns={0: "聚类"}, inplace=True)
    print(result)


if __name__ == '__main__':
    main()
