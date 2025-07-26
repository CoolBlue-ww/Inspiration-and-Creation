from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import random
import time
from selenium.webdriver.common.action_chains import ActionChains
from lxml import etree
from selenium.common.exceptions import TimeoutException
import requests


def offset_browser():
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
    browser.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
        "source": """
          window.chrome = { 
              runtime: {},
              app: { isInstalled: false },
              webstore: {}
          };
          """
    })
    browser.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
        "source": """
          const getParameter = WebGLRenderingContext.prototype.getParameter;
          WebGLRenderingContext.prototype.getParameter = function(parameter) {
              if (parameter === 37445) { // UNMASKED_VENDOR_WEBGL
                  return 'Intel Inc.'; // 伪造显卡厂商
              }
              return getParameter(parameter);
          };
          """
    })

    # 从搜索引擎渗透进入
    browser.get('https://www.baidu.com')
    condition = EC.element_to_be_clickable((By.ID, 'kw'))
    text_box = WebDriverWait(browser, 10).until(condition)
    text_box.send_keys('BOSS直聘')
    # 点击搜索
    button = browser.find_element(By.ID, 'su')
    button.click()

    # 随机延迟
    delay = random.uniform(1.7, 2.5)
    time.sleep(delay)

    # 显示等待
    condition = EC.element_to_be_clickable((By.LINK_TEXT, 'BOSS直聘'))
    button1 = WebDriverWait(browser, 10).until(condition)
    button1.click()

    # IP检测
    # input()

    # 随即延迟
    time.sleep(delay)
    # 切换窗口句柄
    all_windows = browser.window_handles
    browser.switch_to.window(all_windows[-1])

    actions = ActionChains(browser)
    for _ in range(10):
        actions.key_down(Keys.ARROW_DOWN).pause(random.uniform(0, 0.05)).key_up(Keys.ARROW_DOWN).perform()
    for _ in range(10):
        actions.key_down(Keys.ARROW_UP).pause(random.uniform(0, 0.05)).key_up(Keys.ARROW_UP).perform()

    time.sleep(2.5)

    # 输入框
    condition = EC.element_to_be_clickable((By.XPATH, '//div/p[contains(@class, "ipt-wrap")]/input'))
    button1 = WebDriverWait(browser, 10).until(condition)
    location1 = button1.location
    start_x_1 = location1['x']
    start_y_1 = location1['y']

    condition = EC.element_to_be_clickable((By.XPATH, '//div/div[contains(@class, "search-form")]/form/button'))
    button2 = WebDriverWait(browser, 10).until(condition)
    location2 = button2.location
    end_x_1 = location2['x']
    end_y_1 = location2['y']

    return browser, start_x_1, start_y_1, end_x_1, end_y_1, button2, button1


def simulate_human_swipe(browser, start_x_1, start_y_1):
    start_x = 250
    start_y = 160
    actions = ActionChains(browser)
    actions.move_by_offset(start_x, start_y)
    steps = random.randint(8, 14)
    dx = (start_x_1 - start_x) / steps
    dy = (start_y_1 - start_y) / steps

    for i in range(steps):
        offset_x = dx + random.uniform(-3, 2)
        offset_y = dy + random.uniform(-3, 2)
        actions.move_by_offset(offset_x, offset_y)
        actions.pause(random.uniform(0.05, 0.2))
        actions.perform()
    return None


def enter_button(browser):
    condition = EC.element_to_be_clickable((By.XPATH,
                                            '//div[@id="header"]/div/div[contains(@class, "nav-city")]/p/span[contains(@class, "nav-city-selected")]'))
    city_button = WebDriverWait(browser, 10).until(condition)
    actions = ActionChains(browser)
    actions.move_to_element(city_button) \
        .click(city_button) \
        .perform()
    time.sleep(random.uniform(3, 5))
    condition = EC.element_to_be_clickable((By.LINK_TEXT, '全国'))
    button = WebDriverWait(browser, 10).until(condition)
    actions.move_to_element(button) \
        .click(button) \
        .perform()
    condition = EC.element_to_be_clickable((By.XPATH, '//div/p[contains(@class, "ipt-wrap")]/input'))
    button1 = WebDriverWait(browser, 10).until(condition)
    time.sleep(random.uniform(0.9, 1))
    button1.send_keys('p')
    time.sleep(random.uniform(0.1, 0.2))
    button1.send_keys('a')
    button1.send_keys(Keys.BACKSPACE)
    time.sleep(random.uniform(0.03, 0.1))
    button1.send_keys(Keys.BACKSPACE)
    time.sleep(random.uniform(0.1, 0.2))
    button1.send_keys('爬')
    time.sleep(random.uniform(0.1, 0.12))
    button1.send_keys('虫')
    time.sleep(random.uniform(0.1, 0.2))
    button1.send_keys('公')
    time.sleep(random.uniform(0.1, 0.3))
    button1.send_keys(Keys.BACKSPACE)
    time.sleep(random.uniform(0.1, 0.3))
    button1.send_keys('g')
    time.sleep(random.uniform(0.2, 0.3))
    button1.send_keys('o')
    time.sleep(random.uniform(0.2, 0.3))
    button1.send_keys('n')
    time.sleep(random.uniform(0.2, 0.2))
    button1.send_keys('g')
    time.sleep(random.uniform(0.1, 0.2))
    button1.send_keys(Keys.BACKSPACE)
    time.sleep(random.uniform(0.1, 0.2))
    button1.send_keys(Keys.BACKSPACE)
    time.sleep(random.uniform(0.02, 0.1))
    button1.send_keys(Keys.BACKSPACE)
    time.sleep(random.uniform(0.1, 0.3))
    button1.send_keys(Keys.BACKSPACE)
    time.sleep(random.uniform(0.1, 0.2))
    button1.send_keys('工')
    time.sleep(random.uniform(0.1, 0.12))
    button1.send_keys('程')
    time.sleep(random.uniform(0.1, 0.11))
    button1.send_keys('师')
    time.sleep(random.uniform(0.1, 0.13))
    # 回车
    button1.send_keys(Keys.ENTER)
    time.sleep(random.uniform(0.05, 0.1))
    return


def get_job_link(browser):
    first_page_url = browser.current_url

    # BOSS直聘，验证可能具有异常行为的IP的网页, 需要处理点击验证码。
    BOSS_url = 'https://www.zhipin.com/web/user/safe/verify-slider?callbackUrl=https%3A%2F%2Fwww.zhipin.com%2Fweb%2Fgeek%2Fjob%3Fquery%3D%25E7%2588%25AC%25E8%2599%25AB%25E5%25B7%25A5%25E7%25A8%258B%25E5%25B8%2588%26city%3D100010000'

    if first_page_url == BOSS_url:
        print('IP已经被检测出异常行为，进行人工干预！')
        time.sleep(10)
        condition = EC.presence_of_all_elements_located((By.XPATH, '//div/div[contains(@class, "options")]/a'))

        page_button = WebDriverWait(browser, 10).until(condition)

        for i in range(1, len(page_button)):
            actions = ActionChains(browser)
            if i == 7:
                pass
                if i == 5:
                    pass
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
                    for job_href in job_hrefs:
                        job_url = 'https://www.zhipin.com' + job_href
                        return job_url
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
                                return job_url
                            break
                actions.move_to_element(page_button[i]).pause(1.3).click(page_button[i]).perform()
                time.sleep(2)
        print('已经完成所有页面的点击跳转！')
        actions = ActionChains(browser)
        time.sleep(2)
        actions.move_to_element(page_button[7]).pause(1.3).click(page_button[7]).perform()
        page_button = WebDriverWait(browser, 10).until(condition)
        time.sleep(2)
        content = browser.page_source
        if content:
            tree = etree.HTML(content)
            job_hrefs = tree.xpath(
                '//div/div[contains(@class, "search-job-result")]/ul[contains(@class, "job-list-box")]/li/div/a/@href')
            for job_href in job_hrefs:
                job_url = 'https://www.zhipin.com' + job_href
                return job_url
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
                        return job_url
                    break
        for _ in range(90):
            actions \
                .key_down(Keys.ARROW_DOWN) \
                .pause(random.uniform(0, 0.05)) \
                .key_up(Keys.ARROW_DOWN)
        time.sleep(3)
        page_button = WebDriverWait(browser, 10).until(condition)
        actions.move_to_element(page_button[5]).pause(1.3).click(page_button[5]).perform()
        time.sleep(2)
        content = browser.page_source
        if content:
            tree = etree.HTML(content)
            job_hrefs = tree.xpath(
                '//div/div[contains(@class, "search-job-result")]/ul[contains(@class, "job-list-box")]/li/div/a/@href')
            for job_href in job_hrefs:
                job_url = 'https://www.zhipin.com' + job_href
                return job_url
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
                        return job_url
                    break
        browser.quit()
    else:
        job_url_list = []
        condition = EC.presence_of_all_elements_located((By.XPATH, '//div/div[contains(@class, "options")]/a'))

        page_button = WebDriverWait(browser, 10).until(condition)

        for i in range(1, len(page_button)):
            actions = ActionChains(browser)
            if i:
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
                    for job_href in job_hrefs:
                        job_url = 'https://www.zhipin.com' + job_href
                        job_url_list.append(job_url)
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
                                job_url_list.append(job_url)
                            break
                actions.move_to_element(page_button[i]).pause(1.3).click(page_button[i]).perform()
                time.sleep(2)
        print('已经完成所有页面的点击跳转！')
        actions = ActionChains(browser)
        time.sleep(2)
        page_button = WebDriverWait(browser, 10).until(condition)
        actions.move_to_element(page_button[7]).pause(1.3).click(page_button[7]).perform()
        time.sleep(3)
        content = browser.page_source
        if content:
            tree = etree.HTML(content)
            job_hrefs = tree.xpath(
                '//div/div[contains(@class, "search-job-result")]/ul[contains(@class, "job-list-box")]/li/div/a/@href')
            for job_href in job_hrefs:
                job_url = 'https://www.zhipin.com' + job_href
                job_url_list.append(job_url)
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
                        job_url_list.append(job_url)
                    break
        for _ in range(90):
            actions \
                .key_down(Keys.ARROW_DOWN) \
                .pause(random.uniform(0, 0.05)) \
                .key_up(Keys.ARROW_DOWN)
        page_button_min = WebDriverWait(browser, 10).until(condition)
        time.sleep(3)
        actions.move_to_element(page_button_min[5]).pause(1.3).click(page_button_min[5]).perform()
        time.sleep(1)
        content = browser.page_source
        if content:
            tree = etree.HTML(content)
            job_hrefs = tree.xpath(
                '//div/div[contains(@class, "search-job-result")]/ul[contains(@class, "job-list-box")]/li/div/a/@href')
            for job_href in job_hrefs:
                job_url = 'https://www.zhipin.com' + job_href
                job_url_list.append(job_url)
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
                        job_url_list.append(job_url)
                    break
        for _ in range(90):
            actions \
                .key_down(Keys.ARROW_DOWN) \
                .pause(random.uniform(0, 0.05)) \
                .key_up(Keys.ARROW_DOWN)
        browser.quit()
        return job_url_list


def get_content(job_url_list):
    for job_url in job_url_list:
        response = requests.get(job_url)
        content = response.text
        print(content)


def main():
    browser, start_x_1, start_y_1, end_x_1, end_y_1, button2, button1 = offset_browser()
    simulate_human_swipe(browser, start_x_1, start_y_1)
    enter_button(browser)
    job_url_list = get_job_link(browser)
    print(len(job_url_list))
    print(job_url_list)
    get_content(job_url_list)


if __name__ == '__main__':
    main()
