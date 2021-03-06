#  标题：太吝啬内存空间了。

a = 100  # 赋值语句：现在内存中开辟一个空间，保存100这个数字。然后用一个变量a记录保存这个数字的内存位置，一般称谓指向。指针指向。
b = a  # 引用，将a的引用/指向传递给b

# Python中，关于变量的引用，并非在内存中重新开辟一个空间给b。不同于C和C++
# 而是a和b共同指向了a原来指向的内存空间。非常像linux中的软链接。

print(id(a))
print(id(b))



#  特别是在列表中：与C和C++完全不同。
print('#'*22)
A = [11,22,33]
B = A
print(id(A))
print(id(B))

A.append(44)

print(B)


#  总结：Python中任何只要牵扯等号的问题，都是引用。

print('*'*30)
a1 = 100
a2 = 100
a3 = 50 + 50
print(id(a1))
print(id(a2))
print(id(a3))
#  感受一下绝望吧。太能省空间了吧。

