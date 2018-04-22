'''
第 0013 题： 用 Python 写一个爬图片的程序，爬 这个链接里的日本妹子图片 :-) http://tieba.baidu.com/p/2166231880
'''

import urllib.request
from lxml import etree
# 获取网页源代码
def getHtml():
    url = "http://tieba.baidu.com/p/2166231880"
    headers = {"User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4)"}

    request = urllib.request.Request(url, headers=headers)
    response = urllib.request.urlopen(request)
    content = response.read().decode("utf-8")
    return content

# 获取图片
def getImage():
    html = getHtml()
    html = etree.HTML(html)
    links = html.xpath('//img[@class="BDE_Image"]/@src')
    return links

# 下载保存图片
def downloadImage():
    images = getImage()
    for image in images:
        filename = image[-10:]
        with open(filename, 'wb') as f:
            headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4)"}
            request = urllib.request.Request(image, headers=headers)
            response = urllib.request.urlopen(request)
            url = response.read()
            f.write(url)

downloadImage()