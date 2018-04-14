from card import Card
from user import User
from admin import Admin
from atm import ATM
import pickle

def main():
    admin = Admin()
    admin.printAdminView()

    #管理员身份验证
    admin.adminOption()

    # 创建ATM对象
    user_dict = {}
    atm = ATM(user_dict)
    with open(r'd:\code\banksys\allUsers.txt', 'rb') as fr:
        user_dict = pickle.load(fr)
        print(user_dict)

    # 程序如果能够执行到此处表示身份验证是合法的
    while 1:
        admin.printSysFunctionView()
        # 检索功能选项
        value = input('请输入您需要的操作...')
        if value == '1':
            atm.open_account()
        elif value == '2':
            atm.searchUserInfo()
        elif value == '3':
            atm.getMoney()
        elif value == '4':
            atm.saveMoney()
        elif value == '5':
            atm.TransferMoney()
        elif value == '6':
            atm.changePwd()
        elif value == 't':
            # 将字典对象序列化到一个硬盘文件中
            # fw = open('allUsers.txt', 'wb')
            # pickle.dump(allUsers , fw)
            # fw.close()
            with open('allUsers.txt', 'wb') as fw:
                pickle.dump(user_dict, fw)
            return

if __name__ == '__main__':
    main()
