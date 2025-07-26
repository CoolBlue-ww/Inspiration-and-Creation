from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

path = 'chromedriver.exe'
service = Service(path)

browser = webdriver.Chrome(service=service)

url = 'https://www.baidu.com'
browser.get(url)


# 根据id来找到对像
# button = browser.find_element(By.ID, 'su')
# print(button)


# 根据标签属性的属性值来获取对象
# button = browser.find_element(By.NAME, 'wd')
# print(button)


# 根据xpath语句来获取对象
# button = browser.find_element(By.XPATH, '//input[@id="su"]')
# print(button)


# 根据标签的名字来获取对象
# button = browser.find_elements(By.TAG_NAME, 'input')
# print(button)


# 使用bs4的语法来获取对象
# button = browser.find_element(By.CSS_SELECTOR, '#su')
# print(button)


# 定位超链接
button = browser.find_element(By.LINK_TEXT, '新闻')
print(type(button))
