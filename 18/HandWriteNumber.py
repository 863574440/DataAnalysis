from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import numpy as np

digits = load_digits()  # 1797个样本， 每个样本64个特征

features = digits.data
targets = digits.target

train_features, test_features, train_labels, test_labels = \
    train_test_split(features, targets, test_size=0.33)

dtc = DecisionTreeClassifier()
dtc.fit(train_features, train_labels)

predict_labels = dtc.predict(test_features)

# 手动获取正确率
predict_labels = np.array(predict_labels)
test_labels = np.array(test_labels)
score = predict_labels == test_labels
s = list(score).count(True) / len(score)
print(s)

# 使用sklearn计算正确率
ss = accuracy_score(test_labels, predict_labels)
print(ss)
