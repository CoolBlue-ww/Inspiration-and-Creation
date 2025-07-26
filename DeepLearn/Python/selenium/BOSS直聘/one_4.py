from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import random
import time
from selenium.webdriver.common.action_chains import ActionChains
from lxml import etree

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

browser.get('https://www.zhipin.com/web/geek/job?query=%E7%88%AC%E8%99%AB%E5%B7%A5%E7%A8%8B%E5%B8%88&city=100010000')

for _ in range(10):
    condition = EC.presence_of_element_located(
        (By.XPATH, '//div/div[contains(@class, "search-job-result")]/ul[contains(@class, "job-list-box")]/li'))
    button_jobs = WebDriverWait(browser, 10).until(condition)
    content = browser.page_source
    tree = etree.HTML(content)
    jobs = tree.xpath(
        '//div/div[contains(@class, "search-job-result")]/ul[contains(@class, "job-list-box")]/li/div/a/@href')
    for job in jobs:
        url = 'https://www.zhipin.com' + job
        print(url)
    browser.execute_script('window.scrollTo(0, 1000)')
    condition = EC.element_to_be_clickable((By.XPATH, '//div/div[contains(@class, "options")]/a'))
    page_button = WebDriverWait(browser, 10).until(condition)
    print(page_button)
    actions = ActionChains(browser)
    actions.move_to_element(page_button) \
        .click(page_button) \
        .perform()
