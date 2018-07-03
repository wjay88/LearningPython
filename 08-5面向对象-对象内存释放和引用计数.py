class Dog:

    def __del__(self):
        print("-----英雄over----")

dog1 = Dog()
dog2 = dog1

del dog1
del dog2
print("=========="+"***"+"=========")


# 只要对象没人去用之后，那么内存占用的内存就会实时被删除。引用链接数为零时，python解释器会自动释放内存。
# 第10行是否执行，查看打印内容顺序。如果程序结束之前
# 如果执行：那么等到两个del完全删除后，就会把对象删除后需要打印的东西输出。
# 如果不执行，也就说对象不删除，那么在程序结束之后，python解释器也会将所有程序的内存释放。


import sys

# sys.getrefcount()可以查看一个对象多少个引用计数。


class T:
    pass


t = T()
a = sys.getrefcount(t)  # 实际引用个数会多一个，因为该函数会将对象当参数传入内存。

print(a)

tt = t
b = sys.getrefcount(t)
print("b=%d" % b)
