import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
# ax = Axes3D(fig)
# 疑问:上面那句用了以后并不能正常显示3D图像
# 答:原因是直接使用 Axes3D(fig) 并不会将其添加到当前的 figure 中，需要使用 fig.add_axes() 方法。以前的库版本直接用 Axes3D(fig) 就可以显示3D图像。???
ax = fig.add_axes(Axes3D(fig))
# ax = Axes3D(fig)
# ax = fig.add_axes(ax)
# 这两句的意思是
# 第一行创建了一个 3D 坐标轴对象 ax
# 第二行将这个 3D 坐标轴对象添加到当前的 figure 中

# X, Y value
X = np.arange(-4, 4, 0.25)
Y = np.arange(-4, 4, 0.25)
X, Y = np.meshgrid(X, Y)
# meshgrid意思是生成网格点坐标矩阵，用于绘制3D曲面图

R = np.sqrt(X**2 + Y**2)
# height value
Z = np.sin(R)
# 上面的R是每个网格点到原点的距离，当做Z的中间变量

# 绘制3D曲面
ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap="rainbow")
# 意思是绘制一个三维曲面图，X、Y 为网格点坐标，Z 为高度值，rstride 和 cstride 分别表示行和列的步长，cmap 表示颜色映射。

plt.show()
