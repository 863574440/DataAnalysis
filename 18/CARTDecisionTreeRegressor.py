from sklearn.model_selection import train_test_split
from sklearn.datasets import load_boston
from sklearn.metrics import mean_absolute_error, mean_squared_error
from sklearn.tree import DecisionTreeRegressor

# 准备数据集
boston = load_boston()
print(boston.feature_names)  # 506个样本， 每个样本13个特征
features = boston.data
prices = boston.target

train_features, test_features, train_price, test_price = \
    train_test_split(features, prices, test_size=0.33)

# 创建CART回归树
dtr = DecisionTreeRegressor()
# 拟合
dtr.fit(train_features, train_price)

predict_price = dtr.predict(test_features)

print("回归树二乘偏差均值：", mean_squared_error(test_price, predict_price))
print("回归树绝对偏差均值: ", mean_absolute_error(test_price, predict_price))
