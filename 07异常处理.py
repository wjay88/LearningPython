
try:
    11/0
    print(num)
    print("-----1-----")
except (NameError, FileNotFoundError):
    print("如果捕获异常后的处理。。")
except Exception as ret:
    print("如果用了Exception,那么意味着只要上面的except没有捕获到异常，这个except一定会捕获到。")
    print(ret)
else:
    print("没有异常才会执行的功能。")
finally:
    print("无论是否有异常，最后都要做的事。")
    print("-----2------")

# 产品经理与import time
# time.sleep(20)的故事。


# 自定义异常：
class ShortInputException(Exception):

'''自定义的异常类'''

    def __init__(self, length, atleast):
        # super().__init__()
        self.length = length
        self.atleast = atleast


def main():
    try:
        s = input("请输入 -->")
        if len(s) < 3:
            # raise引发一个你定义的异常
            raise ShortInputException(len(s), 3)
    except ShortInputException as result:
        print('ShortInputException:输入的长度是 %d,长度至少应是%d' % (result.length, result.atleast))
    else:
        print("没有异常发生。")

main()




