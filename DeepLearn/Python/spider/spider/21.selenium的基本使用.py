# 第一步，导入selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# 第二步，创建浏览器的操作对象
path = 'chromedriver.exe'
service = Service(path)

browser = webdriver.Chrome(service=service)

# 第三步，访问网站
url = 'https://www.jd.com'

browser.get(url)

# 第四步，page_source获取网页源码
content = browser.page_source
print(content)
