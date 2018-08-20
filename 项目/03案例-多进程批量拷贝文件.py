import os
from multiprocessing import Pool, Manager
import time

'''将该程序放在要拷贝文件夹同路径下。执行。'''


def copyFileTask(name, oldFolderName, newFolderName, queue):
    '''完成copy一个文件的功能'''
    fr = open(oldFolderName+'/'+name)
    fw = open(newFolderName+'/'+name, 'w')

    content = fr.read()
    fw.write(content)

    fr.close()
    fw.close()

    queue.put(name)


def main():
    time1 = time.time()
    # 获取要复制的文件夹名称：
    oldFolderName = input("请输入你要复制的文件夹名称：")

    # 创建新的文件夹：
    newFolderName = oldFolderName + '_复件'
    # print(newFolderName)
    os.mkdir(newFolderName)

    # 获取old文件夹中的所有文件名字：
    filesNames = os.listdir(oldFolderName)
    # print(filesNames)

    # 使用多线程的方式拷贝原文件夹中的文件到新的文件夹中。
    pool = Pool(10)
    queue = Manager().Queue()

    for name in filesNames:
        pool.apply_async(copyFileTask, args=(name, oldFolderName, newFolderName, queue))

    num = 0
    allNum = len(filesNames)
    while True:
        queue.get()
        num += 1
        copyRate = num/allNum
        print('\rcopy的进度是：%.2f%%' % (copyRate*100), end='')
        if num == allNum:
            break
        print('')
    time2 = time.time()
    print('运行时间为：%d s' % (time2 - time1))
    pool.close()
if __name__ == "__main__":
    main()

