# from scrapy import signals
# from selenium import webdriver
# from scrapy.http import HtmlResponse
#
#
# class SeleniumMiddleware(object):
#     def __init__(self):
#         self.driver = webdriver.Chrome()
#
#     def process_request(self, request, spider):
#         self.driver.get(request.url)
#         html = self.driver.page_source
#         return HtmlResponse(self.driver.current_url, body=html, encoding='utf-8', request=request)
#
#     def process_response(self, request, response, spider):
#         return response


# middlewares.py
from scrapy import signals
from scrapy.http import HtmlResponse
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import time


class SeleniumMiddleware:
    def __init__(self, driver_path):
        from selenium import webdriver
        options = webdriver.ChromeOptions()
        # options.add_argument("--headless")  # 无头模式
        # options.add_argument("--disable-gpu")
        self.driver = webdriver.Chrome(options=options)

    @classmethod
    def from_crawler(cls, crawler):
        middleware = cls(driver_path=crawler.settings.get("SELENIUM_DRIVER_PATH"))
        crawler.signals.connect(middleware.spider_closed, signal=signals.spider_closed)
        return middleware

    def spider_closed(self, spider):
        self.driver.quit()

    def process_request(self, request, spider):
        # 仅处理带有 'selenium' 标记的请求
        if not request.meta.get('selenium'):
            return None

        self.driver.get(request.url)

        # 执行自定义操作（从 meta 中获取指令）
        actions = request.meta.get('selenium_actions', [])
        for action in actions:
            if action['type'] == 'input':
                element = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, action['selector']))
                )
                element.send_keys(action['text'])
            elif action['type'] == 'click':
                element = WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, action['selector']))
                )
                element.click()
            time.sleep(2)  # 模拟人类操作间隔
        final_wait = request.meta.get('final_wait', 0)  # 默认不等待
        if final_wait > 0:
            spider.logger.info(f"最后一次操作强制等待 {final_wait} 秒")
            time.sleep(final_wait)  # 强制等待

        # 返回渲染后的页面内容给 Spider
        return HtmlResponse(
            url=self.driver.current_url,
            body=self.driver.page_source.encode('utf-8'),
            encoding='utf-8',
            request=request
        )


# from scrapy import signals
# from scrapy.http import HtmlResponse
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By
# from selenium.common.exceptions import TimeoutException
# import time

# class SeleniumMiddleware:
#     def __init__(self, driver_path):
#         from selenium import webdriver
#         options = webdriver.ChromeOptions()
#         options.add_argument("--headless")
#         options.add_argument("--disable-gpu")
#         self.driver = webdriver.Chrome(options=options)
#
#     @classmethod
#     def from_crawler(cls, crawler):
#         middleware = cls(driver_path=crawler.settings.get("SELENIUM_DRIVER_PATH"))
#         crawler.signals.connect(middleware.spider_closed, signal=signals.spider_closed)
#         return middleware
#
#     def spider_closed(self, spider):
#         self.driver.quit()
#
#     def process_request(self, request, spider):
#         if not request.meta.get('selenium'):
#             return None
#
#         # --- 新增：加载上一个请求传递的 Cookie ---
#         if 'selenium_cookies' in request.meta:
#             self.driver.get('about:blank')  # 清空当前页面
#             for cookie in request.meta['selenium_cookies']:
#                 try:
#                     self.driver.add_cookie(cookie)
#                 except Exception as e:
#                     spider.logger.warning(f"添加 Cookie 失败: {cookie}, 错误: {str(e)}")
#
#         # 访问目标页面
#         self.driver.get(request.url)
#
#         # 执行操作（输入、点击等）
#         actions = request.meta.get('selenium_actions', [])
#         for action in actions:
#             if action['type'] == 'input':
#                 element = WebDriverWait(self.driver, 10).until(
#                     EC.presence_of_element_located((By.CSS_SELECTOR, action['selector']))
#                 )
#                 element.send_keys(action['text'])
#             elif action['type'] == 'click':
#                 element = WebDriverWait(self.driver, 10).until(
#                     EC.element_to_be_clickable((By.CSS_SELECTOR, action['selector']))
#                 )
#                 element.click()
#             time.sleep(1)
#
#         # --- 新增：将当前 Cookie 存入响应 meta，供下一个请求使用 ---
#         return HtmlResponse(
#             url=self.driver.current_url,
#             body=self.driver.page_source.encode('utf-8'),
#             encoding='utf-8',
#             request=request,
#             meta={
#                 'selenium_cookies': self.driver.get_cookies()  # 捕获当前所有 Cookie
#             }
#         )