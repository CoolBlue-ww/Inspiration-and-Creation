from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import random
import time

# 创建浏览器实例
service = webdriver.ChromeService(executable_path="D:\pt2\Scripts\chromedriver.exe")
options = Options()
# options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-gpu')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--disable-blink-features=AutomationControlled')
options.add_argument('--disable-infobars')
options.add_argument('--disable-web-security')
browser = webdriver.Chrome(service=service, options=options)

# 从搜索引擎渗透进入
browser.get('https://www.baidu.com')
condition = EC.element_to_be_clickable((By.ID, 'kw'))
text_box = WebDriverWait(browser, 10).until(condition)
text_box.send_keys('BOSS直聘')
# 点击搜索
button = browser.find_element(By.ID, 'su')
button.click()

# 随机延迟
delay = random.uniform(1.7, 2.5)
time.sleep(delay)

# 显示等待
condition = EC.element_to_be_clickable((By.LINK_TEXT, 'BOSS直聘'))
button1 = WebDriverWait(browser, 10).until(condition)
button1.click()

# 随即延迟
time.sleep(delay)
# 切换窗口句柄
all_windows = browser.window_handles
browser.switch_to.window(all_windows[-1])

# 轻微滚动
obj_button = 'document.documentElement.scrollTop=100'
browser.execute_script(obj_button)

# 模拟用户搜索
button2_1 = browser.find_element(By.XPATH, '//div/p[contains(@class, "ipt-wrap")]/input')
button2_1.send_keys('爬')
# 随机延迟
time.sleep(delay)
button2_2 = browser.find_element(By.XPATH, '//div/p[contains(@class, "ipt-wrap")]/input')
button2_2.send_keys('虫')
# 随机延迟
time.sleep(delay)
button2_3 = browser.find_element(By.XPATH, '//div/p[contains(@class, "ipt-wrap")]/input')
button2_3.send_keys('工')
# 随机延迟
time.sleep(delay)
button2_4 = browser.find_element(By.XPATH, '//div/p[contains(@class, "ipt-wrap")]/input')
button2_4.send_keys('程')
# 随机延迟
time.sleep(delay)
button2_5 = browser.find_element(By.XPATH, '//div/p[contains(@class, "ipt-wrap")]/input')
button2_5.send_keys('师')

# 随机延迟
time.sleep(delay)
button3 = browser.find_element(By.XPATH, '//div/div[contains(@class, "search-form")]/form/button')
button3.click()

# 显示等待+强制等待 模拟用户切换自己想要就业的城市。
condition = EC.presence_of_all_elements_located((By.XPATH, '//div/div[contains(@class, "area-dropdown-item")]/ul/li[3]'))
button4 = WebDriverWait(browser, 10).until(condition)
time.sleep(5)
button4.click()
print(button4)
input()