import tensorflow as tf

# 创建一个EagerTensor
a = tf.constant([1, 2, 3, 4, 5])

# 直接访问其numpy值
print(a.numpy())  # 输出：[1 2 3 4 5]

# 使用Python控制流
if tf.reduce_sum(a) > 10:
    print("The sum is greater than 10")  # 这将执行并打印
