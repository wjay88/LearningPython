#  完成连个变量的交换

a = 4
b = 5
#  第一种做法：引入第三变量：升维
c = a
a = b
b = c

#  第二种做法：要求没有引入第三个变量。
a=a+b
b=a-b
a=a-b
#  这种写法在任何语言中都实用。

#  第三种做法：
a, b = b, a
#  Python所独自拥有的。
