# 框架：
"""
实现增删改查的功能，先用过程，再改为函数，然后引入文件。

"""


def title():

    print("*"*25)
    print("*  \033[1;34;40m名片信息系统 V 1.0 \033[0m *")
    print("*"*25)

infoSys = []  # 整体信息集合
info = {}   # 个体信息
iID = 0     # 编号，引申为操作日志。
SwID = []   # 被删除编号。
count = 0   # 统计总和



def prompt():

    print("1:增加名片信息")
    print("2:删除名片信息")
    print("3:修改名片信息")
    print("4:查询名片信息")
    print("5:遍历名片信息")
    print("6:保存数据信息")
    print("0:退出信息系统")


# 增加
def add_person(sname, sage, saddr):
    global SwID
    global iID
    global infoSys
    global count

    # 新增成员之前查看编号集合中是否有删除未用的元素。若有则分配。
    if len(SwID) != 0:
        sID = SwID[0]
        del (SwID[0])
    # 若无则继续排序。
    else:
        iID = iID + 1
        sID = iID
    # 成员信息元。
    info = {'ID': sID, 'name': sname, 'age': sage, 'addr': saddr}
    infoSys.append(info)
    print(info)
    count = count + 1


# 查找
def find_person(fname):
    # exist_person = None
    # 不要在for循环中打印if-else情况满足不满足的情况，会被多次遍历。需要加上标识变量。
    find_flag = 0  # 默认表示没有找到。这为常用方法。
    for item in infoSys:
        while fname in item['name']:
            find_flag = 1
            exist_person = item
            print("此人存在！", exist_person)
            break  # 此处添加一个break

    # 判断是否找到：i
    if find_flag == 0:
        print("查无此人，请确认您的输入。")


def del_person(del_name):
    global SwID
    global iID
    global infoSys
    global count
    for info1 in infoSys:
        if del_name == info1['name']:
            SwID.append(info1['ID'])
            SwID.sort()
            infoSys.remove(info1)
            print("%s has deleted。" % info1['name'])
            count = count - 1
    print(infoSys)
    print("SwID = %s" % SwID)
    print("当前总数：%d" % count)


# 修改
def alter_person(al_name):
    global infoSys
    for item in infoSys:
        if item["name"] == al_name:
            print(item)
            opt = input("请输入您要修改的项目(name? age? or addr?)：")
            if opt in ['name', 'age', 'addr']:
                change = input("请输入修改后的内容：")
                item[opt] = change
                print(item)
            else:
                print("请输入您要修改的项目：内容限定为：name、age、addr")


def load_info():
    l = []
    global infoSys, count, iID, SwID
    try:  # 如果文件不存在，捕获异常。
        f = open("name.data")
        f1 = open("arg.data")
        for line in f.readlines():
            infoSys.append(eval(line))
            count = count + 1
            l.append(eval(line)['ID'])

        iID = max(l)  # 此处必须是先转换，变成字典然后调取。
        SwID = eval(f1.read())   # eval函数方法可以将字符串本来的格式还原出来。
        return infoSys, count, SwID, iID
        f.close()
        f1.close()
    except Exception:
        pass


def save_data():
    f = open("name.data", 'w')
    global infoSys, count, SwID
    for item in infoSys:
        f.write(str(item)+'\n')  # 此处必须是str才可以写入。
    f.close()
    f1 = open("arg.data", 'w')
    f1.write(str(SwID))
    f1.close()
    print("保存成功！")


# 完成对整个程序的控制：
def main():

    # 恢复之前的数据到程序中。
    load_info()

    title()
    prompt()
    global infoSys

    while True:

        try:
            num = int(input("\n请输入您要操作的序号："))
            # 增
            if num == 1:
                add_name = input("\t请输入你要添加的姓名：")
                add_age = input("\t请输入你要添加的年龄：")
                add_addr = input("\t请输入你要添加的地址：")
                add_person(add_name, add_age, add_addr)

            # 删
            elif num == 2:
                input_del = input("请输入您要删除的姓名：")
                del_person(input_del)

            # 改
            elif num == 3:
                alter_name = input("请输入您要修改的姓名：")
                alter_person(alter_name)

            # 查
            elif num == 4:
                find_name = input("请输入您要查找的人员姓名：")
                find_person(find_name)

            # 遍历
            elif num == 5:
                for item in infoSys:
                    print(item)
                print("\n当前总人数：%d 人" % count)

            # 保存数据
            elif num == 6:
                save_data()

            # 退出
            elif num == 0:
                print("。。。退出信息系统。。。")
                break
            else:
                prompt()
        except Exception as e:
            print("\033[1;34;40m！！！输入无效！！！请输入指定序号！！！！\033[0m")
            prompt()


if __name__ == '__main__':
    main()

# 可完善部分是：如果对象存在，函数之间应该可以传递改对象。
# 而且修改功能中不应该增加for功能查找。
# 待修改：修改输入错误之后，重新保留在添加输入项上面。


# 总结：函数中引入全局变量必须实现声明：global。
# 在文件中保存内容只能为数字或字符串类型。
# 所以读取的时候，也要通过eval()来转换其类型。
# 参数文件单独保存：arg.data。
# 后续研究多个参数读取问题。划分行保存，对行读取。


