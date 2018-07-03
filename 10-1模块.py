# 模块：一个py文件。系统自带的。
# pip install pygame

# pip 是管理python模块的工具。pip2 install pygame和pip3 install pygame

import os
print(os.__file__)

# .pyc字节码文件。将import加载模块加载到内存生成的文件。
if __name__ == '__main__':
    test1()
    test2()
    main()
# 当别人调用时不执行，当自己调用时执行。


模块中：__all__ = ["test1", "test2"]
当别人在调用from 该模块名 import *形式。就会将all中函数或全局变量调用。