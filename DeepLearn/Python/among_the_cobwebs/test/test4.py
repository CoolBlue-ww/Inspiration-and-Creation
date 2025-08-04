from among_the_cobwebs.automation.WebDriver.system.windows.edge.request_data import RequestData

from selenium import webdriver
from selenium.webdriver.edge.service import Service
e = RequestData(platform='win64', version='138.0.351.121').install()
ser = Service(e)
dr = webdriver.Edge(service=ser)
dr.get('https://www.baidu.com')

