from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import random
import time
from selenium.webdriver.common.action_chains import ActionChains



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
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-browser-side-navigation")
prefs = {
    "profile.managed_default_content_settings.images": 1,
    "permissions.default.stylesheet": 1
}
options.add_experimental_option("prefs", prefs)
browser = webdriver.Chrome(service=service, options=options)

browser.get('https://www.zhipin.com/chengshi/c101250300/?seoRefer=index')

condition = EC.element_to_be_clickable((By.XPATH, '//div[@id="header"]/div/div[contains(@class, "nav-city")]/p/span[contains(@class, "nav-city-selected")]'))
city_button = WebDriverWait(browser, 10).until(condition)
actions = ActionChains(browser)
actions.move_to_element(city_button)\
    .click(city_button)\
    .perform()
time.sleep(5)
condition = EC.element_to_be_clickable((By.LINK_TEXT, '全国'))
button = WebDriverWait(browser, 10).until(condition)
actions.move_to_element(button).click(button).perform()


input()

