from selenium import webdriver
import time
from lxml import etree

chromedriver = r"d://chromedriver.exe"
driver = webdriver.Chrome(chromedriver)
driver.get("https://www.zhihu.com/question/36011809")
driver.execute_script("window.scrollTo(0,4000)")
response = etree.HTML(driver.page_source)

# print(response)
answers = response[0].xpath(r'//div[@class="List-item"]')

print(answers)