# CART 分类树
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.datasets import load_iris

# 准备数据集
iris = load_iris()

# 获取特征值和分类标识
features = iris.data  # 150个样本 每个样本四个特征
labels = iris.target  # 150个样本名

# 随机选取三分之一作为测试集
train_features, test_features, train_labels, test_labels = \
    train_test_split(features, labels, test_size=0.33)

# 创建CART分类树树
clf = DecisionTreeClassifier(criterion="gini")  #

# 拟合CART树
clf.fit(train_features, train_labels)
# 用CART分类树做预测
test_predict = clf.predict(test_features)

# 预测结果与真实结果做对比
score = accuracy_score(test_labels, test_predict)
print("CART分类树准确率 %.4lf" % score)
