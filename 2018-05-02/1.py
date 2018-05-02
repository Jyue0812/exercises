from selenium import webdriver
import time


driver = webdriver.Firefox()
driver.get("https://www.zhihu.com/question/36011809")
driver.execute_script("window.scrollTo(0,400000)")
response = driver.page_source
print(response)