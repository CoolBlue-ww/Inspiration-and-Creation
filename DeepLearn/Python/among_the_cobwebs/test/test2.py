from among_the_cobwebs.automation.WebDriver.system.windows.install import ChromeDriver


p = ChromeDriver(clean_registry=True, clean_json_api=True).install()

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

ser = Service(p)
dr = webdriver.Chrome(service=ser)
dr.get('https://www.baidu.com/')


