import numpy as np

person_type = np.dtype({"names": ["name", "Chinese", "English", "Math"],
                        "formats": ["S32", "i", "i", "i"]})

persons = np.array([("zhangfei", 66, 65, 30),
                    ("guanyu", 95, 85, 98),
                    ("zhaoyun", 93, 92, 96),
                    ("huangzhong", 90, 88, 77),
                    ("dianwei", 80, 90, 90)], dtype=person_type)

ch = persons[:]["Chinese"]
en = persons[:]["English"]
ma = persons[:]["Math"]
scores = np.array([ch, en, ma])
print(scores)

print("姓名           | 平均 | 最小 | 最大 | 方差 | 标准")
for a, b, c, d, e, f in zip(persons["name"], np.mean(scores, axis=0), np.min(scores, axis=0),
                            np.max(scores, axis=0), np.var(scores, axis=0), np.std(scores, axis=0)):
    print("%-15s %4.2f %4.2f %4.2f %4.2f %4.2f" % (a, b, c, d, e, f))

for i in sorted(persons, key=lambda x: sum([x["Chinese"], x["English"], x["Math"]]), reverse=True):
    print(i)

print(persons[:]["name"])
