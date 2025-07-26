from selenium import webdriver
from selenium.common import TimeoutException
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


def get_job_link(browser):
    first_page_url = browser.current_url

    # BOSS直聘，验证可能具有异常行为的IP的网页, 需要处理点击验证码。
    BOSS_url = 'https://www.zhipin.com/web/user/safe/verify-slider?callbackUrl=https%3A%2F%2Fwww.zhipin.com%2Fweb%2Fgeek%2Fjob%3Fquery%3D%25E7%2588%25AC%25E8%2599%25AB%25E5%25B7%25A5%25E7%25A8%258B%25E5%25B8%2588%26city%3D100010000'

    if first_page_url == BOSS_url:
        # print('IP已经被检测出异常行为，退出浏览器实例！')
        # browser.quit()
        print('IP已经被检测出异常行为，进行人工干预！')
        time.sleep(10)
        condition = EC.presence_of_all_elements_located((By.XPATH, '//div/div[contains(@class, "options")]/a'))

        page_button = WebDriverWait(browser, 10).until(condition)

        job_page_url_7 = first_page_url + '&page=7'

        job_page_url_9 = first_page_url + '&page=9'

        for i in range(1, len(page_button)):
            actions = ActionChains(browser)
            if i == 6:
                browser.get(job_page_url_7)
                time.sleep(3)
                content = browser.page_source
                if content:
                    tree = etree.HTML(content)
                    job_hrefs = tree.xpath(
                        '//div/div[contains(@class, "search-job-result")]/ul[contains(@class, "job-list-box")]/li/div/a/@href')
                    print(len(job_hrefs))
                    for job_href in job_hrefs:
                        job_url = 'https://www.zhipin.com' + job_href
                        print(job_url)
                else:
                    print('网页内容未能加载完成！')
                    page_url = browser.current_url
                    while True:
                        browser.get(page_url)
                        actions \
                            .key_down(Keys.F5) \
                            .pause(random.uniform(0, 0.05)) \
                            .key_up(Keys.F5)
                        content = browser.page_source
                        if content:
                            tree = etree.HTML(content)
                            job_hrefs = tree.xpath(
                                '//div/div[contains(@class, "search-job-result")]/ul[contains(@class, "job-list-box")]/li/div/a/@href')
                            print(len(job_hrefs))
                            for job_href in job_hrefs:
                                job_url = 'https://www.zhipin.com' + job_href
                                print(job_url)
                            break
                if i == 8:
                    browser.get(job_page_url_9)
                    time.sleep(3.45)
                    content = browser.page_source
                    if content:
                        tree = etree.HTML(content)
                        job_hrefs = tree.xpath(
                            '//div/div[contains(@class, "search-job-result")]/ul[contains(@class, "job-list-box")]/li/div/a/@href')
                        print(len(job_hrefs))
                        for job_href in job_hrefs:
                            job_url = 'https://www.zhipin.com' + job_href
                            print(job_url)
                    else:
                        print('网页内容未能加载完成！')
                        page_url = browser.current_url
                        while True:
                            browser.get(page_url)
                            actions \
                                .key_down(Keys.F5) \
                                .pause(random.uniform(0, 0.05)) \
                                .key_up(Keys.F5)
                            content = browser.page_source
                            if content:
                                tree = etree.HTML(content)
                                job_hrefs = tree.xpath(
                                    '//div/div[contains(@class, "search-job-result")]/ul[contains(@class, "job-list-box")]/li/div/a/@href')
                                print(len(job_hrefs))
                                for job_href in job_hrefs:
                                    job_url = 'https://www.zhipin.com' + job_href
                                    print(job_url)
                                break
            else:
                try:
                    page_button = WebDriverWait(browser, 10).until(condition)
                except TimeoutException:
                    print('触发爬虫检测次数过多，最大等待时长已耗尽！')
                    page_url = browser.current_url
                    while True:
                        browser.get(page_url)
                        page_button = WebDriverWait(browser, 10).until(condition)
                        if page_button:
                            break
                if i == 1:
                    for _ in range(90):
                        actions \
                            .key_down(Keys.ARROW_DOWN) \
                            .pause(random.uniform(0, 0.05)) \
                            .key_up(Keys.ARROW_DOWN)
                    for _ in range(10):
                        actions \
                            .key_down(Keys.ARROW_UP) \
                            .pause(random.uniform(0, 0.05)).key_up(Keys.ARROW_UP) \
                            .key_up(Keys.ARROW_UP) \
                            .perform()
                else:
                    for _ in range(90):
                        actions \
                            .key_down(Keys.ARROW_DOWN) \
                            .pause(random.uniform(0, 0.05)) \
                            .key_up(Keys.ARROW_DOWN)
                content = browser.page_source
                if content:
                    tree = etree.HTML(content)
                    job_hrefs = tree.xpath(
                        '//div/div[contains(@class, "search-job-result")]/ul[contains(@class, "job-list-box")]/li/div/a/@href')
                    print(len(job_hrefs))
                    for job_href in job_hrefs:
                        job_url = 'https://www.zhipin.com' + job_href
                        print(job_url)
                else:
                    print('网页内容未能加载完成！')
                    page_url = browser.current_url
                    while True:
                        browser.get(page_url)
                        actions \
                            .key_down(Keys.F5) \
                            .pause(random.uniform(0, 0.05)) \
                            .key_up(Keys.F5)
                        content = browser.page_source
                        if content:
                            tree = etree.HTML(content)
                            job_hrefs = tree.xpath(
                                '//div/div[contains(@class, "search-job-result")]/ul[contains(@class, "job-list-box")]/li/div/a/@href')
                            for job_href in job_hrefs:
                                job_url = 'https://www.zhipin.com' + job_href
                                print(job_url)
                            break
                actions.move_to_element(page_button[i]).pause(1.3).click(page_button[i]).perform()
                time.sleep(2)
        print('已经完成所有页面的点击跳转！')
        browser.quit()
    else:
        condition = EC.presence_of_all_elements_located((By.XPATH, '//div/div[contains(@class, "options")]/a'))

        page_button = WebDriverWait(browser, 10).until(condition)

        job_page_url_7 = first_page_url + '&page=7'

        job_page_url_9 = first_page_url + '&page=9'

        for i in range(1, len(page_button)):
            actions = ActionChains(browser)
            if i == 6:
                browser.get(job_page_url_7)
                time.sleep(3)
                content = browser.page_source
                if content:
                    tree = etree.HTML(content)
                    job_hrefs = tree.xpath(
                        '//div/div[contains(@class, "search-job-result")]/ul[contains(@class, "job-list-box")]/li/div/a/@href')
                    print(len(job_hrefs))
                    for job_href in job_hrefs:
                        job_url = 'https://www.zhipin.com' + job_href
                        print(job_url)
                else:
                    print('网页内容未能加载完成！')
                    page_url = browser.current_url
                    while True:
                        browser.get(page_url)
                        actions \
                            .key_down(Keys.F5) \
                            .pause(random.uniform(0, 0.05)) \
                            .key_up(Keys.F5)
                        content = browser.page_source
                        if content:
                            tree = etree.HTML(content)
                            job_hrefs = tree.xpath(
                                '//div/div[contains(@class, "search-job-result")]/ul[contains(@class, "job-list-box")]/li/div/a/@href')
                            print(len(job_hrefs))
                            for job_href in job_hrefs:
                                job_url = 'https://www.zhipin.com' + job_href
                                print(job_url)
                            break
                if i == 8:
                    browser.get(job_page_url_9)
                    time.sleep(3.45)
                    content = browser.page_source
                    if content:
                        tree = etree.HTML(content)
                        job_hrefs = tree.xpath(
                            '//div/div[contains(@class, "search-job-result")]/ul[contains(@class, "job-list-box")]/li/div/a/@href')
                        print(len(job_hrefs))
                        for job_href in job_hrefs:
                            job_url = 'https://www.zhipin.com' + job_href
                            print(job_url)
                    else:
                        print('网页内容未能加载完成！')
                        page_url = browser.current_url
                        while True:
                            browser.get(page_url)
                            actions \
                                .key_down(Keys.F5) \
                                .pause(random.uniform(0, 0.05)) \
                                .key_up(Keys.F5)
                            content = browser.page_source
                            if content:
                                tree = etree.HTML(content)
                                job_hrefs = tree.xpath(
                                    '//div/div[contains(@class, "search-job-result")]/ul[contains(@class, "job-list-box")]/li/div/a/@href')
                                print(len(job_hrefs))
                                for job_href in job_hrefs:
                                    job_url = 'https://www.zhipin.com' + job_href
                                    print(job_url)
                                break
            else:
                try:
                    page_button = WebDriverWait(browser, 10).until(condition)
                except TimeoutException:
                    print('触发爬虫检测次数过多，最大等待时长已耗尽！')
                    page_url = browser.current_url
                    while True:
                        browser.get(page_url)
                        page_button = WebDriverWait(browser, 10).until(condition)
                        if page_button:
                            break
                if i == 1:
                    for _ in range(90):
                        actions \
                            .key_down(Keys.ARROW_DOWN) \
                            .pause(random.uniform(0, 0.05)) \
                            .key_up(Keys.ARROW_DOWN)
                    for _ in range(10):
                        actions \
                            .key_down(Keys.ARROW_UP) \
                            .pause(random.uniform(0, 0.05)).key_up(Keys.ARROW_UP) \
                            .key_up(Keys.ARROW_UP) \
                            .perform()
                else:
                    for _ in range(90):
                        actions \
                            .key_down(Keys.ARROW_DOWN) \
                            .pause(random.uniform(0, 0.05)) \
                            .key_up(Keys.ARROW_DOWN)
                content = browser.page_source
                if content:
                    tree = etree.HTML(content)
                    job_hrefs = tree.xpath(
                        '//div/div[contains(@class, "search-job-result")]/ul[contains(@class, "job-list-box")]/li/div/a/@href')
                    print(len(job_hrefs))
                    for job_href in job_hrefs:
                        job_url = 'https://www.zhipin.com' + job_href
                        print(job_url)
                else:
                    print('网页内容未能加载完成！')
                    page_url = browser.current_url
                    while True:
                        browser.get(page_url)
                        actions \
                            .key_down(Keys.F5) \
                            .pause(random.uniform(0, 0.05)) \
                            .key_up(Keys.F5)
                        content = browser.page_source
                        if content:
                            tree = etree.HTML(content)
                            job_hrefs = tree.xpath(
                                '//div/div[contains(@class, "search-job-result")]/ul[contains(@class, "job-list-box")]/li/div/a/@href')
                            for job_href in job_hrefs:
                                job_url = 'https://www.zhipin.com' + job_href
                                print(job_url)
                            break
                actions.move_to_element(page_button[i]).pause(1.3).click(page_button[i]).perform()
                time.sleep(2)
        print('已经完成所有页面的点击跳转！')
        browser.quit()
    return None
