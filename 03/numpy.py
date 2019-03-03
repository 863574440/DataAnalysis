import numpy as np

person = np.dtype({"names": ["name", "age", "height"],
                   "formats": ["S32", "i", "f"]})

a = np.array([("lisi", 12, 170), ("zhangsan", 23, 199)], dtype=person)
print(a.dtype)

a = np.ndarray([2, 2], dtype=np.int32, )
print(a)

print(type(np.array([1, 2, 4])))

a = np.random.randn(2, 3)
print(a)

a = np.array([[1, 2, 3],
              [2, 3, 4]])

print(np.max(a, axis=1))
print(np.sum(a, axis=0))

