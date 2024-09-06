import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 定义电荷的参数
k = 8.9875517923 * (10 ** 9)  # 真空中的静电力常数
q1 = 1  # 第一个电荷的电荷量
q2 = 1  # 第二个电荷的电荷量
r1 = np.array([1, 0, 0])  # 第一个电荷的位置
r2 = np.array([-1, 0, 0])  # 第二个电荷的位置

# 定义要绘制的空间网格
x = np.linspace(-2, 2, 100)
y = np.linspace(-2, 2, 100)
X, Y = np.meshgrid(x, y)

# 计算每个点上的电势
V1 = k * q1 / np.sqrt((X - r1[0])**2 + (Y - r1[1])**2)
V2 = k * q2 / np.sqrt((X - r2[0])**2 + (Y - r2[1])**2)
V_total = V1 + V2

# 绘制等势面图像
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# 绘制等势面
surf = ax.plot_surface(X, Y, V_total, cmap='viridis')

# 添加标签和标题
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Electric Potential')
ax.set_title('Electric Potential of Two Like Charges')

# 添加颜色条
fig.colorbar(surf, shrink=0.5, aspect=5)

# 显示图像
plt.show()