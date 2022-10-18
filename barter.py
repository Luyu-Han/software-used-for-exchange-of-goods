import os

filename = 'barter.txt'


class Barter:
    def __init__(self, totalList):
        self.totalList = totalList
        if os.path.exists(filename):
            file = open(filename, 'r', encoding='utf-8')
            self.totalList = file.readlines()
        else:
            self.totalList = []

    def run(self):
        while True:
            self.showMenu()
            choice = int(input('请选择您需要的功能'))
            if choice in [0, 1, 2, 3, 4, 5]:
                if choice == 0:
                    answer = input('您确定要退出系统吗？y/n')
                    if answer == 'y' or answer == 'Y':
                        print('感谢您的使用')
                        break
                    else:
                        continue
                elif choice == 1:
                    self.addItem()
                elif choice == 2:
                    self.delItem()
                elif choice == 3:
                    self.showList()
                elif choice == 4:
                    self.modify()
                elif choice == 5:
                    self.search()
            else:
                print('请确认所需功能，重新输入0-5之间的数字')

    def addItem(self):

        item_list = []

        while True:
            item = input("请输入可交换的物品名称：")
            if not item:
                break
            togive = input("请输入您的姓名：")
            if not togive:
                break
            giveNum = input("请输入您的联系方式：")
            if not giveNum:
                break
            note = input("任何您想说的话：")
            if not note:
                break

            itemInformation = {'物品名称': item, '交换人': togive, '交换人联系方式': giveNum, '备注': note}
            item_list.append(itemInformation)

            answer = input('是否继续添加？y/n\n')  # 后一个\n表示换行
            if answer == 'y':
                continue
            else:
                break

        self.save(item_list)
        print('物品信息录入完毕')

    def delItem(self):
        while True:
            item = input('请输入要删除的物品名称：')
            if item != '':
                flag = False
                if self.totalList:
                    with open(filename, 'w', encoding='utf-8') as wfile:
                        item_dic = {}
                        for i in self.totalList:
                            item_dic = dict(eval(i))  # 将字符串转化为字典
                            if item_dic['物品名称'] != item:
                                wfile.write(str(item_dic) + '\n')
                            else:
                                flag = True
                        if flag:
                            print(f'物品{item}已被删除')
                        else:
                            print(f'没有找到物品{item}的信息')
                else:
                    print('列表中尚未存储物品信息')
                    break
                self.showList()
                answer = input('是否继续删除？y/n\n')
                if answer == 'y':
                    continue
                else:
                    break

    def showList(self):
        if os.path.exists(filename):
            file = open(filename, 'r', encoding='utf-8')
            self.totalList = file.readlines()
        else:
            self.totalList = []
        if self.totalList:
            for i in self.totalList:
                print(i)
        else:
            print('暂未保存过数据')

    def showMenu(self):
        if os.path.exists(filename):
            with open(filename, 'r', encoding='utf-8') as file:
                self.totalList = file.readlines()
        else:
            self.totalList = []
        print('==========================“你帮我助”物品交换========================')
        print('-----------------------------功能菜单-----------------------------')
        print('                         1. 创建可交换物品信息')
        print('                         2. 删除物品信息')
        print('                         3. 显示所有信息')
        print('                         4. 修改信息')
        print('                         5. 搜索物品信息')
        print('                         0. 退出系统')
        print('----------------------------------------------------------------')

    def modify(self):
        self.showList()
        i = input('请输入欲修改信息/想进行交换的物品名称：')
        wfile = open(filename, 'w', encoding='utf-8')
        for item in self.totalList:
            item_dic = dict(eval(item))
            if item_dic['物品名称'] == i:
                print('已找到物品信息，可继续进行修改')
                while True:
                    choice = int(input("请选择修改的信息（修改交换人姓名输入1，交换人联系方式输入2，与换人姓名3，与换人联系方式4，备注5）："))
                    if choice == 1:
                        item_dic['交换人'] = input('请输入交换人姓名：')
                    elif choice == 2:
                        item_dic['交换人联系方式'] = input('请输入交换人联系方式：')
                    elif choice == 3:
                        item_dic['与换人'] = input('请输入与换人姓名：')
                    elif choice == 4:
                        item_dic['与换人联系方式'] = input('请输入与换人联系方式：')
                    elif choice == 5:
                        item_dic['备注'] = input('请输入新的备注：')
                    else:
                        print("请重新输入1-5中的数字")
                    break
                wfile.write(str(item_dic) + '\n')
                print('已修改成功')
            else:
                wfile.write(str(item_dic) + '\n')
        answer = input('是否继续修改其它物品信息？y/n\n')
        if answer == 'y':
            self.modify()

    def search(self):
        query = []  # 放在列表中而非字典，可以避免重名导致的报错
        while True:
            item = ''
            togive = ''
            toreceive = ''
            if self.totalList:
                mode = input('按物品名称查找请输入1，按交换人姓名查找请输入2，按与换人姓名查找请输入3')
                if mode == '1':
                    item = input('请输入要查找的物品名称：')
                elif mode == '2':
                    togive = input('请输入交换人姓名：')
                elif mode == '3':
                    toreceive = input('请输入与换人姓名：')
                else:
                    print('您的输入有误，请重新输入数字1-3')
                    continue

                for i in self.totalList:
                    item_dic = dict(eval(i))
                    if item != '':
                        if item_dic['物品名称'] == item:
                            query.append(item_dic)
                    elif togive != '':
                        if item_dic['交换人'] == togive:
                            query.append(item_dic)
                    elif toreceive != '':
                        if item_dic['与换人'] == toreceive:
                            query.append(item_dic)

                self.showInfo(query)
                query.clear()
                answer = input('是否要继续查询？y/n\n')
                if answer == 'y':
                    continue
                else:
                    break
            else:
                print('暂未保存过数据')
                return

    def showInfo(self, query):
        if len(query) == 0:
            print('没有查询到相关信息，无数据显示')
        print(query)

    def save(self, lst):
        stu_txt = open(filename, 'a', encoding='utf-8')  # 以追加的模式打开
        for item in lst:
            stu_txt.write(str(item) + '\n')
        stu_txt.close()


if __name__ == '__main__':
    total_lst = []
    barter = Barter(total_lst)
    barter.run()
