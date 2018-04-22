import urllib.request
from lxml import etree
import ssl

url = "xxx"
headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 6.1; WOW64)"}
request = urllib.request.Request(url, headers=headers)
context = ssl._create_unverified_context()
ssl._create_default_https_context = ssl._create_unverified_context()
response = urllib.request.urlopen(request, context=context)
content = response.read()

html = etree.HTML(content)
links = html.xpath("//dd/a/@href")
name = html.xpath("//dd/a/text()")

for link in links:
    new_link = url +link[-8:]
    request1 = urllib.request.Request(new_link, headers=headers)
    response1 = urllib.request.urlopen(request1)
    content1 = response1.read().decode("gbk","ignore")
    html1 = etree.HTML(content1)
    zhengwen = html1.xpath('//div[@class="content"]/text()')
    for zw in zhengwen:
        zw.replace(r"\xa0","")
        print(zw)
        with open("baijie.txt", "a") as f:
            f.write(zw)
