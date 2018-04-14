'''
atm：
类名：ATM
属性：字典(卡号-用户)
行为：开户   查询  取款  存款  转账  改密  退出
'''
import random
from card import Card
from user import User


class ATM:
    def __init__(self, user_dict):
        self.user_dict = user_dict

    # 开户
    def open_account(self):
        # 从键盘输入用户的一些信息：name、idCard、phone
        name = input('请输入用户的名字：')
        idCard = input('请输入用户的身份证号：')
        phone = input('请输入用户的手机号：')
        preStoreMoney = int(input('请输入预存款金额：'))

        # 判断预存款金额
        if preStoreMoney <= 0:
            print('预存款金额输入有误！开户失败...')
            return -1


        onePasswd = input('请设置密码：')
        # 验证密码：
        if not self.checkPasswd(onePasswd):
            print('密码输入有误！开户失败...')
            return -1

        #开卡
        idCard = self.createCardnum()
        # 创建card和user对象
        card = Card(idCard, onePasswd, preStoreMoney)
        user = User(name, idCard, phone, card)

        # 将卡号和用户加入到字典中
        self.user_dict[idCard] = user
        print('开户成功！请牢记卡号(%s)...' % (idCard))

    # 查询
    def searchUserInfo(self):
        # 验证卡号是否存在
        # cardId = input('请输入卡号：')
        # user = self.allUsers.get(cardId)
        user = self.checkUser()
        if not user:
            print('该卡号不存在，查询失败...')
            return -1

        # 验证密码
        if not self.checkPasswd(user.card.card_pwd):
            print('输入的密码有误，查询失败...')
            return -1

        print('卡号：%s    余额：%d' % (user.card.card_num, user.card.card_money))

    #生成卡号
    def createCardnum(self):
        while 1:
            str1 = ''
            #随机生成六位数
            for i in range(6):
                ch = str(random.randint(0, 9))
                str1 += ch
            #要是在已经生成的卡号中取不到，就生成卡号
            if not self.user_dict.get(str1):
                return str1

    # 取款
    def getMoney(self):
        # 验证卡号是否存在
        cardId = input('请输入卡号：')
        user = self.user_dict.get(cardId)
        user = self.checkUser()
        if not user:
            print('该卡号不存在，取款失败...')
            return -1

        # 验证密码
        if not self.checkPasswd(user.card.card_pwd):
            print('密码输入有误，取款失败...')
            return -1

        # 验证取款金额是否合法
        money = int(input('请输入取款金额：'))
        if money > user.card.card_money:
            print('余额不足，取款失败...')
            return -1

        if money <= 0:
            print('输入的值有误，取款失败...')
            return -1

        user.card.card_money -= money
        print('取款成功...')

    # 存款
    def saveMoney(self):
        # 验证卡号是否存在
        user = self.checkUser()
        if not user:
            print('该卡号不存在，存款失败...')
            return

        # 验证密码
        if not self.checkPasswd(user.card.card_pwd):
            print('密码输入有误，存款失败...')
            return

        # 进行存款操作&校验
        money = int(input('请输入存款金额：'))
        if money <= 0:
            print('输入的值有误，取款失败...')
            return -1

        user.card.card_money += money
        print('存款成功...')

    def TransferMoney(self):
        #验证转出和转入的卡号是否存在
        # outUser = self.checkUser()
        # inUser = self.checkUser()
        outId = input('请输入转出卡号：')
        outUser = self.user_dict.get(outId)

        if not outUser:
            print('转出的卡号不存在，转账失败...')
            return -1

        inId = input('请输入转入卡号：')
        inUser = self.user_dict.get(inId)

        if not inUser:
            print('转入的卡号不存在，转账失败...')
            return -1

        #验证转出卡号密码
        if not self.checkPasswd(outUser.card.card_pwd):
            print('密码输入有误！转账失败...')

        #开始转账，并且验证金额问题
        money = int(input('请输入转账金额：'))

        if money <= 0:
            print('输入的值有误，转账失败...')
            return -1

        if money > outUser.card.card_money:
            print('余额不足，转账失败...')
            return -1

        outUser.card.card_money -= money
        inUser.card.card_money += money

        print('转账成功...')

    #改密码
    def changePwd(self):
        user = self.checkUser()
        if not user:
            print('该卡号不存在，存款失败...')
            return

        # 验证密码
        if not self.checkPasswd(user.card.card_pwd):
            print('密码输入有误，失败...')
            return

        new_pwd = input('新密码：')
        self.checkPasswd(new_pwd)
        user.card.card_pwd = new_pwd
        print('保存成功')

    # 验证密码
    def checkPasswd(self, realPasswd):
        # 确认密码(3次机会)
        i = 3
        while i > 0:
            tempPasswd = input('请输入密码：(%d次)' %i)
            if realPasswd == tempPasswd:
                return True
            i -= 1
        return False


#验证用户是否存在
    def checkUser(self):
        cardId = input('请输入卡号：')
        user = self.user_dict.get(cardId)
        return user