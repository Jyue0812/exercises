'''
第 0008 题： 一个HTML文件，找出里面的正文。
第 0009 题： 一个HTML文件，找出里面的链接。
https://pypi.org/project/lxml/
'''
import urllib.request
from lxml import etree

def spider():
    url = "https://pypi.org/project/lxml/"
    headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 6.1; WOW64)"}
    request = urllib.request.Request(url, headers=headers)
    response = urllib.request.urlopen(request)
    content = response.read()
    return content.decode('utf-8')

html = spider()
# print(html)
html = etree.HTML(html)


links = html.xpath("//a/@href")
links2 = html.xpath("//img/@src")
new_links = links + links2

count = 0
result = []
for l in new_links:
    if str(l).startswith("https"):
        result.append(l)

print(result, len(result))

# def parse():
#     links = html.find(r'/a')
#     print(links)
#     # print(html_list)
#     # for hl in html_list:
#     #     write(hl.strip())
#
# def write(item):
#     with open('d://code/lianjie.txt', 'a') as f:
#         f.write(item)
#
# parse()

