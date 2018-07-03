a=100
l=[100]
def test(num):
    '''总结：如果指针指向了一个可变数据类型-列表。可以直接修改。
            如果指向了不可变类型-整数，则无法修改。
            此时用的是：num+=num。此处就是修改值。
    '''
    num+=num
    print(num)

test(a)
print(a)
print("------我是分割线-----")
test(l)
print(l)

print("-----以下内容很重要！-----")


def test2(num):
    '''
        此时采用num = num + num。先算等式右边。
    '''
    num = num + num
    print(num)

test2(a)
print(a)
test2(l)
print(l)  #  此时的l却没有改变。

print("总结：num+=num和num=num + num并不等价。\n\t一个是操作修改，发现操作数据可变，直接修改内存。\n\t一个先算右边，产生新的数值,新的内存存储后交给左边，\n\t但是其原来的内存存储的不变。")