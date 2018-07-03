def test1(a, b, c=22, *args, **kwargs):
    print("-"*30)
    print(a)
    print(b)
    print(c)
    print(args)
    print(kwargs)

    # result = a+b
    # for num in args:
    #     result += num
    # print("result = %d"%result)

test1(11, 22, 33, 44, 55, 66, 77, num1=88, num2=99)
print(11+22+33+44+55+66+77)  #c

A = (44, 55, 66)
B = {"name": 'laowang', "age": 18}
test1(11, 22, 33, A, B) #不拆包的情况，全部进入到元组中。

test1(11,22,33,*A,**B)  #拆包：在元组和字典前加*，完成一个个元素传入。
# 进程线程创建的时候会用到这个功能。