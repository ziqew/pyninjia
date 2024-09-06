import numpy as np

# 使用 numpy 创建 ndarray
arr_np = np.array([1, 2, 3, 4, 5])

# 使用 Python 原生列表
arr_list = [1, 2, 3, 4, 5]

# numpy 的矢量化运算
squared_np = arr_np ** 2

# Python 原生列表的循环运算
squared_list = [x ** 2 for x in arr_list]

# 性能对比（对于大型数据集，numpy 的性能优势更加明显）
