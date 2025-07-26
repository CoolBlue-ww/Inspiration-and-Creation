from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

path = 'chromedriver.exe'
service = Service(path)
# 获取浏览器对象
browser = webdriver.Chrome(service=service)

url = 'https://www.baidu.com'

# 驱动真实浏览器向服务器发送请求
browser.get(url)

input = browser.find_element(By.ID, 'su')

# 获取标签的属性
print(input.get_attribute('class'))
# 获取标签的名字
print(input.tag_name)

a = browser.find_element(By.LINK_TEXT, '新闻')

# 获取标签的文本信息
print(a.text)
print(a.get_attribute('href'))



a.click()

time.sleep(10)