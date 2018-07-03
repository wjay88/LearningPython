# 文件定位读写seek()
# f=open("test.txt")
# f.seek(,0) # 偏移量。
# f.seek(0,0) # 文件指针重新回到开头。
# f.tell() #告知文件指针位置。


# 文件、文件夹操作。
import os
# os.rename("","")
# os.remove("")
# os.mkdir("")
# os.rmdir("")
# os.getcwd()  # 获取当前路径
# os.chdir("../")
# os.listdir("./")


# 1、获取要重命名的文件夹的名字
folder_name = input("请输入您要重命名的文件夹:")
# 2、获取指定的文件夹中的所有的文件名称
file_names = os.listdir(folder_name)
os.chdir(folder_name)
# 3、重命名
num = 0
for name in file_names:
    if os.path.getsize(name) <= 50000:
        os.remove(name)
        print(name+"\tdeleted")
    else:
        num = num + 1
        os.rename(name, str(num) + ".jpg")
print(num)