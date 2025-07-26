from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import random

# 创建浏览器对象
path = 'chromedriver.exe'
service = Service(path)
browser = webdriver.Chrome(service=service)

url = 'https://www.baidu.com'

# 驱动真实浏览器访问网站
browser.get(url)
# 随机延迟
delay = random.uniform(1, 2)
time.sleep(delay)

# 获取文本框对象
input = browser.find_element(By.ID, 'kw')

# 在文本框中输入周杰伦
input.send_keys('周杰伦')
# 等待两秒
time.sleep(2)

# 获取百度一下按钮
button = browser.find_element(By.ID, 'su')

# 点击按钮
button.click()
time.sleep(2)

# 滑到底部
js_bottom = 'document.documentElement.scrollTop = 100000'
browser.execute_script(js_bottom)
time.sleep(2)

# 下一页
next_button = browser.find_element(By.XPATH, '//a[@class="n"]')
next_button.click()
time.sleep(2)

# 回到上一页
browser.back()
time.sleep(2)

# 后悔了再回去
browser.forward()
time.sleep(5)

# 退出浏览器
browser.quit()