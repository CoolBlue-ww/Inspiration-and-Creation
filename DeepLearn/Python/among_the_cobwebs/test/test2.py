from among_the_cobwebs.automation.WebDriver.system.windows.chrome.install import ChromeDriver


p = ChromeDriver().install()

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

ser = Service(p)
dr = webdriver.Chrome(service=ser)
dr.get('https://www.baidu.com/')


