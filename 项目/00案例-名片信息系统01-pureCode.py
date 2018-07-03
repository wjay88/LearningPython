# 框架：
"""
实现增删改查的功能，先用过程，再改为函数，然后引入文件。

"""
print("*"*25)
print("*  \033[1;34;40m名片信息系统 V 1.0 \033[0m *")
print("*"*25)
print("1:增加名片信息")
print("2:删除名片信息")
print("3:修改名片信息")
print("4:查询名片信息")
print("5:遍历名片信息")
print("0:退出信息系统")

infoSys = []  # 整体信息集合
info = {}   # 个体信息
iID = 0     # 编号，引申为操作日志。
SwID = []   # 被删除编号。
count = 0   # 统计总和
while True:
    try:
        num = int(input("\n请输入您要操作的序号："))

        # 增
        if num == 1:
            Sname = input("\t请输入你要添加的姓名：")
            Sage = input("\t请输入你要添加的年龄：")
            Saddr = input("\t请输入你要添加的地址：")
            # 新增成员之前查看编号集合中是否有删除未用的元素。若有则分配。
            if SwID != []:
                SID = SwID[0]
                del(SwID[0])
            # 若无则继续排序。
            else:
                iID = iID + 1
                SID = iID
            # 成员信息元。
            info = {'ID': SID, 'name': Sname, 'age': Sage, 'addr': Saddr}
            infoSys.append(info)
            print(info)
            count = count + 1

        # 删
        elif num == 2:
            Sdel = input("请输入您要删除的姓名：")
            for info1 in infoSys:
                if Sdel == info1['name']:
                    SwID.append(info1['ID'])
                    SwID.sort()
                    infoSys.remove(info1)
                    print("%s has deleted。" % info1['name'])
                    count = count - 1
            print(infoSys)
            print("SwID = %s" % SwID)
            print("当前总数：%d" % count)

        # 改
        elif num == 3:
            Cname = input("请输入您要修改的姓名：")
            for item in infoSys:
                if item["name"] == Cname:
                    print(item)
                    opt = input("请输入您要修改的项目(name? age? or addr?)：")
                    if opt in ['name', 'age', 'addr']:
                        change = input("请输入修改后的内容：")
                        item[opt] = change
                        print(item)
                    else:
                        print("请输入您要修改的项目：内容限定为：name、age、addr")
                else:
                    print("无此信息，请核对你的输入！或输入5查询所有人员信息。")

        # 查
        elif num == 4:
            Fname = input("请输入您要查找的人员姓名：")
            # 不要在for循环中打印if-else情况满足不满足的情况，会被多次遍历。需要加上标识变量。
            find_flag = 0  # 默认表示没有找到。这为常用方法。
            for item in infoSys:
                while Fname in item['name']:
                    print('此人存在:', item)
                    find_flag = 1
                    break  # 此处添加一个break

            # 判断是否找到：
            if find_flag == 0:
                print("查无此人，请确认您的输入。")
        # 遍历
        elif num == 5:
            for item in infoSys:
                print(item)

        # 退出
        elif num == 0:
            print("。。。退出信息系统。。。")
            break
        else:
            print("请输入数字0~5 ：！")
            print("1:增加名片信息")
            print("2:删除名片信息")
            print("3:修改名片信息")
            print("4:查询名片信息")
            print("5:遍历名片信息")
            print("0:退出信息系统\n")
    except Exception as e:
        print("\033[1;34;40m！！！输入无效！！！请输入指定序号！！！！\033[0m")
        print("1:增加名片信息")
        print("2:删除名片信息")
        print("3:修改名片信息")
        print("4:查询名片信息")
        print("5:遍历名片信息")
        print("0:退出信息系统\n")
    # finally:
    #     print("=====================程序运行中===================")


# 可完善部分是：根据编号排序，然后记录操作日志等等。





