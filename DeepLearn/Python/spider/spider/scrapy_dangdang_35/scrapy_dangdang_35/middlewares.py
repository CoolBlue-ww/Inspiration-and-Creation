# 导入所需要的库
from scrapy import signals
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from scrapy.http import HtmlResponse
from webdriver_manager.chrome import ChromeDriverManager


class SeleniumMiddleware:
    def __init__(self):
        # 初始化selenium浏览器实例
        options = Options()
        options.add_argument("--headless")  # 启用无头浏览器模式
        options.add_argument("--disable-gpu")
        self.driver = webdriver.Chrome(options=options)

    @classmethod
    def from_crawler(cls, crawler):
        # 通过crawler对象初始化中间件
        middleware = cls()
        crawler.signals.connect(middleware.spider_closed, signal=signals.spider_opened)
        return middleware

    def process_request(self, request, spider):
        # 检查请求是否需要Selenium
        if request.meta.get('selenium'):
            try:
                self.driver.get(request.url)
                body = self.driver.page_source.encode('utf-8')
                return HtmlResponse(self.driver.current_url, body=body, encoding='utf-8', request=request)
            except Exception as e:
                spider.logger.error(f'Selenium error:{e}')
                return HtmlResponse(self.driver.current_url, status=504, request=request)
        return None

    def spider_closed(self, spider):
        self.driver.quit()
