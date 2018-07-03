import sys


name = sys.argv[1]  # 此处选择第1个参数，也可以从1往后[1:]，也可以选择其他。
print("热烈欢迎%s的到来。" % name)

# 总结：给程序传递参数：
# 测试的时候在cmd窗口中运行：python 模块传参数.py 狼王
