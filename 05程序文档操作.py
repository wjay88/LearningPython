# 在linux中一切皆文件。
#  程序的数据都在内存中，防止丢失，必须保存到文件中本地固化下来。


'''
在程序中打开文件，程序如何对待文件。用open函数。
第一个参数:文件名。第二个参数：
    r：只读文件必须存在，否则报错。默认可以不写。
    w：只写：文件可以不存在。不存在就创建。
        如果文件已经存在，那么就覆盖。
    a：追加。文件指针从开头开始，如果不存在，创建新文件。
    rb:带b的表示二进制。
        文件分类:
            1、文本文件：编辑器编辑。
            2、二进制文件：比如一张图片。
            cpu处理数据来自于内存。内存从硬盘和网络读取数据。硬盘只能存储01010数据。
    r+:带+号表示：读写。

open函数打开之后返回值保存到一个变量中f
后续通过f来操作。因为f已经指向了打开的内容
f.close()关闭文件。操作完成。

作业：
完成文件备份。
'''

#1、获取用户要复制的文件名
old_file_name = input("请输入你要复制的文件名：")
#2、打开要复制的文件
old_file = open(old_file_name, 'r')
position = old_file_name.rfind(".")
new_file_name = old_file_name[:position] + "[复件]" + old_file_name[position:]
# 3、新建一个文件
new_file = open(new_file_name,'w')

# 4、从旧文件中读取数据，写入到新文件中。
# content = old_file.read()
# new_file.write(content)
while True:
    content = old_file.read(1024)

    if len(content) == 0:
        break
    new_file.write(content)


# 5、关闭2个文件。
old_file.close()
new_file.close()




