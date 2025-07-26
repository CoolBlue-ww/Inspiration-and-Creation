# 用新学的selenium和xpath再再次尝试爬取站长素材上的建筑图片
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
import random
from lxml import etree
import urllib.request


# 建立get_content函数来获取每一页网页的HTML源码
def get_content(page, browser):
    if page == 1:
        url = 'https://sc.chinaz.com/tupian/tesejianzhutupian.html'
    else:
        url = 'https://sc.chinaz.com/tupian/tesejianzhutupian_' + str(page) + '.html'
    # 随机延迟
    delay = random.uniform(0.5, 1.5)
    time.sleep(delay)
    # 向服务器发送请求
    browser.get(url)
    # 获取到响应的数据
    content = browser.page_source
    return content


# 建立img_urls函数来获取图片的下载地址和图片对应的名字
def img_urls(content):
    # 对获取到的网页源码进行解析
    tree = etree.HTML(content)
    # 查找图片的名字和下载地址
    name_list = tree.xpath('//div[contains(@class, "小猫图片-list com-img-txt-list masonry")]//img/@alt')
    src_list = tree.xpath('//div/div/div/img/@data-original')
    return name_list, src_list


# 对图片进行下载
def download_img(name_list, src_list):
    for i in range(len(name_list)):
        name = name_list[i]
        src = src_list[i]
        url = 'https:' + src
        urllib.request.urlretrieve(url=url, filename='./爬取站长素材的建筑图片/' + name + '.jpg')


# 建立一个主函数
def main():
    start_page = int(input("请输入开始页码："))
    end_page = int(input("请输入结束页码："))
    # 制定模拟浏览器对象，初始化浏览器
    path = 'chromedriver.exe'
    service = Service(path)
    browser = webdriver.Chrome(service=service)
    for page in range(start_page, end_page + 1):
        # 主要运行的函数
        content = get_content(page, browser)
        name_list, src_list = img_urls(content)
        download_img(name_list, src_list)
    print("已完成所有下载")


if __name__ == '__main__':
    main()
