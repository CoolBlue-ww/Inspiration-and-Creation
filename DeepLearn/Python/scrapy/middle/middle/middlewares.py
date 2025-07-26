from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.chrome.options import Options
from scrapy.http import HtmlResponse
from webdriver_manager.chrome import ChromeDriverManager
from scrapy import signals
import fake_useragent

class SeleniumMiddleware(object):
    def __init__(self):
        ua = fake_useragent.UserAgent()
        self.user_agent = ua.random
        self.service = Service(executable_path=r"X:\桌面\chromedriver\chromedriver-win64\chromedriver-win64\chromedriver.exe", log_output="chromedriver.log", port=8080)
        self.options = Options()
        self.options.add_argument(f"user-agent={self.user_agent}")
        self.browser = webdriver.Chrome(service=self.service, options=self.options)

    @classmethod
    def from_crawler(cls, crawler):
        middleware = cls()
        crawler.signals.connect(middleware.spider_closed, signal=signals.spider_closed)
        return middleware

    def process_request(self, request, spider):

        self.browser.execute_cdp_cmd("Network.setExtraHTTPHeaders", {"headers": {"User-Agent": self.user_agent}})

        self.browser.get(request.url)
        body = self.browser.page_source
        return HtmlResponse(self.browser.current_url, body=body, encoding="utf-8", request=request)

    def process_response(self, request, response, spider):
        return response

    def spider_closed(self, spider):
        self.browser.quit()
