def functionD():
    global p
    p = 100  # global关键字可以在函数内部修改全局变量的值
    print("the p is", p)
    return p + 999  # 返回p的值


print(p)
# 老师那边直接这样打印,会报错,逻辑是,函数D还没有被调用,所以p还没有被定义(更别提什么全局变量),所以会报错
# 疑问:但是不知道为什么这里可以输出,所以py的编译顺序到底是什么样的?

# print(functionD())  # 调用函数, 并打印返回值
# print(p)  # 函数内部的全局变量可以在函数外部使用
