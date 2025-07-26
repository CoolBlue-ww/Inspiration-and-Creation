# 再次优化代码的结构，使其更加模块化。对站长素材图片进行再次爬取。
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random
import urllib.request
from lxml import etree
# 引入本地文件作为脚本来初始化加载浏览器并开起无头模式
import ChromeHandless


# 调用脚本里面的chromehandless函数

# 建立一个函数用来切换浏览器窗口句柄
def switch_window(browser):
    all_windows = browser.window_handles
    browser.switch_to.window(all_windows[-1])
    return


# 定义一个函数用来自动滚动到当前页面的底部
def page_bottom(browser):
    js_button = 'document.documentElement.scrollTop=100000'
    browser.execute_script(js_button)
    return


# 制定一个函数用来逐步点击进入目标网页
def enter_page(browser, picture_type):
    url = 'https://www.baidu.com'
    # 驱动浏览器打开目标网站
    browser.get(url)
    # 随机延迟，模拟用户等待百度的加载
    delay = random.uniform(1.5, 2.5)
    time.sleep(delay)
    # 定义等待条件
    condition = EC.element_to_be_clickable((By.ID, 'kw'))
    input_text = WebDriverWait(browser, 10).until(condition)
    # 输入想要搜索的内容——站长素材官网
    input_text.send_keys('站长素材')
    # 间隔0.5秒
    time.sleep(0.5)
    # 点击确认，进行搜索
    button = browser.find_element(By.ID, 'su')
    button.click()
    # 延迟两秒模拟用户在寻找目标信息
    time.sleep(2)
    # 进入站长素材官方网站
    condition = EC.element_to_be_clickable((By.LINK_TEXT, '站长素材-分享综合设计素材免费下载的平台'))
    zhanzhang_button = WebDriverWait(browser, 10).until(condition)
    zhanzhang_button.click()
    # 睡眠三秒模拟用户在寻找自己想要的目标
    time.sleep(3)
    # 调用switch_window()函数切换窗口句柄
    switch_window(browser)
    # 点击进入高清图片页面
    picture_button = browser.find_element(By.LINK_TEXT, '高清图片')
    picture_button.click()
    # 切换窗口句柄
    switch_window(browser)
    # 在暂停两秒模拟用户正在选择自己喜欢的图片类型。
    time.sleep(2)
    condition = EC.element_to_be_clickable((By.LINK_TEXT, str(picture_type)))
    FJ_button = WebDriverWait(browser, 10).until(condition)
    FJ_button.click()
    # 再做一次窗口句柄切换
    switch_window(browser)
    return


# 建立一个函数用来获取当前网页源码
def get_content(browser):
    content = browser.page_source
    return content


# 建立函数来获取图片的下载地址
def get_urls(content):
    # 解析网页源码
    tree = etree.HTML(content)
    # 查找图片的src属性和图片的名字
    src_list = tree.xpath('//div/div/div/img/@data-original')
    name_list = tree.xpath('//div[contains(@class, "小猫图片-list com-img-txt-list masonry")]//img/@alt')
    return name_list, src_list


# 建立download_img函数对图片进行下载
def download_img(name_list, src_list):
    for i in range(len(name_list)):
        name = name_list[i]
        src = src_list[i]
        url = 'https:' + src
        urllib.request.urlretrieve(url=url, filename='./再次优化结合selenium交互尝试对站长素材图片进行再次爬取/' + name + '.png')
        print(f'{name},下载成功!')


# 建立主函数
def main(browser):
    content = get_content(browser)
    name_list, src_list = get_urls(content)
    download_img(name_list, src_list)


# 建立一个函数用来循环执行主函数，以此来下载多页的图片内容。
def main_loop():
    start_page = int(input('请输入开始页码：'))
    end_page = int(input('请输入结束页码：'))
    picture_type = input('请输入你喜欢的照片类型（例如：人物图片，风景图片等）：')
    # 初始化定制浏览器
    browser = ChromeHandless.chromehandless()
    # 逐步驱动浏览器进入目标网页
    enter_page(browser, picture_type)
    while start_page <= end_page:
        # 重复执行主函数对多页图片进行下载
        main(browser)
        # 模仿用户滑倒底部，点击下一页
        page_bottom(browser)
        next_page = browser.find_element(By.XPATH, '//a[@class="nextpage"]')
        next_page.click()
        # 切换浏览器窗口句柄
        switch_window(browser)
        start_page += 1
        # 随机延迟，模拟用户等待新页面的加载
        delay = random.uniform(1.5, 2.5)
        time.sleep(delay)


if __name__ == '__main__':
    main_loop()
    print("已经执行完成所有的操作！")
