import urllib.request
import re

class Spider:
    def __init__(self):
        self.page = 2
        self.switch = True


    def loadPage(self):
        '''
        下载页面
        '''
        url = "http://www.neihan8.com/article/index_" + str(self.page) + ".html"
        print(url)
        headers = {"User-Aagent" : "Mozilla/5.0 (Windows NT 6.1; WOW64)"}
        request = urllib.request.Request(url, headers=headers)
        response = urllib.request.urlopen(request)
        html = response.read().decode('utf-8')

        pattern = re.compile('<div\sclass="desc">(.*?)</div>', re.S)
        content_list = pattern.findall(html)

        self.dealPage(content_list)

    def dealPage(self, content_list):
        '''
        处理每页的段子
        '''
        for item in content_list:
            item = item.replace(r'&amp;',' ').replace(r'hellip;','').replace(r'&mdash;','')
            self.writePage(item)

    def writePage(self,item):
        '''
        把每条段子逐个写入文件里
        '''
        with open('d://code/duanzi.txt','a') as f:
            f.write(item)


    def startWork(self):
        '''
        控制爬虫运行
        '''
        while self.switch:
            command = input("继续爬去请按回车，退出请按quit")
            if command == "quit":
                self.switch = False
            self.loadPage()
            self.page += 1


if __name__ == '__main__':
    s = Spider()
    s.loadPage()
    s.startWork()