import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

fig, ax = plt.subplots()

x = np.arange(0, 2 * np.pi, 0.01)
# 意思是生成从0到2π，步长为0.01的数组，用于绘制x轴的数据
y = np.sin(x)
(line,) = ax.plot(x, y)
# line后加,是因为ax.plot返回的是一个包含Line2D对象的列表，而我们只需要第一个元素，所以用逗号解包。疑问: 那后面的元素是什么
# 实际上是列表中的其他Line2D对象，如果有多条曲线同时绘制，就会有多个Line2D对象。


# (jypter里显示不出动画,只能显示静态图像,要放在py里看)
def animate(i):
    line.set_ydata(np.sin(x + i / 10))
    return (line,)


def init():
    line.set_ydata(np.sin(x))
    return (line,)


ani = animation.FuncAnimation(
    fig, animate, init_func=init, frames=100, interval=20, blit=True
)
# 每个参数意思是:
# fig: 要进行动画的图形对象
# animate: 更新每一帧的函数，这里是更新line的y数据
# init_func: 初始化函数，用于设置动画的初始状态 (因为前面还有个参数要填,而我们这里不填,所上面要指明init_func=)
# frames: 总帧数
# interval: 每帧之间的时间间隔，单位是毫秒
# blit: 是否只重绘发生变化的部分，设置为True可以提高动画性能，但在某些情况下可能导致显示问题。

plt.show()
