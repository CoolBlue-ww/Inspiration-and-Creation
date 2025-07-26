import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
path = 'chromedriver.exe'
service = Service(path)
browser = webdriver.Chrome(service=service)

url = ''
browser.get(url)
# time.sleep(2)
condition = EC.presence_of_element_located((By.TAG_NAME, 'ul'))
# time.sleep(2)
WebDriverWait(browser, 10).until(condition)
time.sleep(5)
content = browser.page_source
print(content)
# https://www.zhipin.com/web/common/security-check.html?seed=fo4GqNBhGTKMA3Lc1uxTj544rWqtBLiwU5JALx5j0Oo%3D&name=87b7f462&ts=1741675285632&callbackUrl=https%3A%2F%2Fwww.zhipin.com%2Fweb%2Fgeek%2Fjob%3Fquery%3D%25E5%2585%25A8%25E6%25A0%2588%25E5%25B7%25A5%25E7%25A8%258B%25E5%25B8%2588%26city%3D101020100%26page%3D2