#  动态编译
def test(a, b, func):
    result = func(a, b)
    return result
func_new = input("请输入一个匿名函数:")
func_new = eval(func_new)
num = test(11, 22, func_new)
print(num)

'''
这个程序如果放在python2中执行就对，如果放在3中执行报错。
原因：input在python2中
在python3中，全部看作是一个字符串。所以必须使用eval函数来操作。
'''

