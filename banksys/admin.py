'''
管理员：
类名：Admin
属性：管理员的用户名  管理员的密码
行为：系统欢迎界面   验证管理员信息  系统功能界面
'''

import time

class Admin:
    # 类属性：用户名和密码
    admin = '1'
    passwd = '1'

    def printAdminView(self):
        print("*****************************************************************")
        print("*                                                               *")
        print("*                                                               *")
        print("*                        欢迎登陆 VIP 银行                       *")
        print("*                                                               *")
        print("*                                                               *")
        print("*****************************************************************")

    def printSysFunctionView(self):
        print("*****************************************************************")
        print("*        开户(1)                            查询(2)             *")
        print("*        取款(3)                            存款(4)             *")
        print("*        转账(5)                            改密(6)             *")
        print("*                         退出(t)                               *")
        print("*****************************************************************")

    # 验证管理员信息
    def adminOption(self):
        input_admin = input('请输入管理员帐号：')
        if self.admin != input_admin:
            print('输入管理员帐号有误！')
            return -1
        input_passwd = input('请输入管理员密码：')
        if self.passwd != input_passwd:
            print('输入密码有误')
            return -1

        # 如果程序能够执行到此处，说明管理员帐号和密码是没有问题的
        print('操作成功！请稍候...')
        time.sleep(0.5)
        return 0