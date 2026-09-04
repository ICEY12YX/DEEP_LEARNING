import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-1, 1, 50)
# 意思是生成从-1到1的50个等间距的数值(绘图用的50个点)
y = 2 * x + 1
# y也是50个点
plt.plot(x, y)
# 绘制x和y的关系曲线
# 疑问:这个函数到底怎么用的
plt.show()
# 意思是显示绘制的图像

x = np.linspace(-3, 3, 50)
y1 = 2 * x + 1  # 线性函数
y2 = x**2  # 二次函数

# 可以调节参数
plt.figure()
plt.plot(x, y1, color="r", linewidth=1, linestyle="--")
plt.plot(x, y2)

plt.xlim(-1, 2)  # 设置x轴的范围
# 老师那边是这样写的plt.xlim((-3, 3))
# 疑问:为什么有些函数里可以加括号,或者不加
plt.ylim(-2, 3)  # 设置y轴的范围
plt.xlabel("I am x")  # 设置x轴的标签
plt.ylabel("I am y")  # 设置y轴的标签

# plt.xlabel("x轴")  # 设置x轴的标签
# plt.ylabel("y轴")  # 设置y轴的标签
# 但是用中文,会报错 疑问:待解决

new_ticks = np.linspace(-1, 2, 5)  # 设置新的刻度
print(new_ticks)
plt.xticks(new_ticks)  # 设置x轴的刻度
# plt.yticks(
#     [-2, -1.8, -1, 1.22, 3], ["really low", "low", "medium", "high", "really high"]
# )  # 设置y轴的刻度

plt.yticks(
    [-2, -1.8, -1, 1.22, 3], ["$really\ low$", "low", "medium", "high", "really high"]
)  # 设置y轴的刻度

plt.show()
