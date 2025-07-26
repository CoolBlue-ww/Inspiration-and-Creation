from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import fake_useragent

# path = r"X:\桌面\chromedriver\chromedriver-win64\chromedriver-win64\chromedriver.exe"

service = Service()

driver = webdriver.Chrome(service=service)

driver.get("https://www.baidu.com")

ua = fake_useragent.UserAgent()

print(ua.random)

driver.execute("Network.enable", {})


def ls(event):
    request = event["request"]
    print(f"Request Url: {request['url']}")
    print(f"Request Headers: {request['headers']}")


driver.add_cdp_listener("Network.requestWillBeSent", ls)

driver.get("https://www.baidu.com")

driver.quit()
