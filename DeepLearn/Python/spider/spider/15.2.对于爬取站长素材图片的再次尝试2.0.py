# 爬取站长素材小猫第一页的尝试
import urllib.request
from bs4 import BeautifulSoup
import time
import random


# 建立原始地请求对象
def create_request(page):
    if page == 1:
        base_url = 'https://sc.chinaz.com/tupian/xiaomaotupian.html'
    else:
        base_url = 'https://sc.chinaz.com/tupian/xiaomaotupian_' + str(page) + '.html'

    headers = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,"
                  "application/signed-exchange;v=b3;q=0.7",
        # "accept-encoding": "gzip, deflate, br, zstd",
        "accept-language": "zh-CN,zh;q=0.9",
        "cache-control": "max-age=0",
        "cookie": "cz_statistics_visitor=60e39643-f700-9f0a-4758-985e0bcb0e1a; _clck=gwrfib%7C2%7Cftn%7C0%7C1874; Hm_lvt_398913ed58c9e7dfe9695953fb7b6799=1740129597,1740196172,1740196831,1740197792; HMACCOUNT=B339802B59031595; Hm_lpvt_398913ed58c9e7dfe9695953fb7b6799=1740207560",
        "priority": "u=0, i",
        "referer": "https://sc.chinaz.com/tupian/",
        "sec-ch-ua": "\"Not(A:Brand\";v=\"99\", \"Google Chrome\";v=\"133\", \"Chromium\";v=\"133\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "document",
        "sec-fetch-mode": "navigate",
        "sec-fetch-site": "same-origin",
        "sec-fetch-user": "?1",
        "upgrade-insecure-requests": "1"
    }
    request = urllib.request.Request(url=base_url, headers=headers)
    return request


# 获取原始页面的响应数据
def get_content(request):
    # 随机延迟
    delay = random.uniform(0.5, 1.5)
    time.sleep(delay)
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')
    return content


# 获取每种图片对应的小猫的名字
def get_name(content):
    soup = BeautifulSoup(content, 'lxml')
    # 初始化一个列表用来储存小猫名字
    name_list = []
    alt_list = soup.select('div > div > div > img[alt]')
    for alt in alt_list:
        name = alt.get('alt')
        name_list.append(name)
    return name_list


# 获取原始页面中每张图片的链接地址
def get_links(content):
    url_list = []
    soup = BeautifulSoup(content, 'lxml')
    a_list = soup.select('div > div > div > div > a.name')
    for a in a_list:
        href = a.get('href')
        url_list.append('https://sc.chinaz.com' + href)
    return url_list


# 对每个超链接发送请求进行访问，获取图片原始地下载地址
def get_img_urls(url_list):
    # 随机延迟
    delay = random.uniform(0.5, 1.5)
    time.sleep(delay)
    # 初始化一个列表，用来储存每张图片真实地下载地址
    True_url_list = []
    for url in url_list:
        response = urllib.request.urlopen(url)
        content = response.read().decode('utf-8')
        soup = BeautifulSoup(content, 'lxml')
        img = soup.select('div >div > div > div > div > img[alt]')
        # print(img)
        True_url = 'https:' + img[0].get('src')
        True_url_list.append(True_url)
    return True_url_list


# 对图片进行下载
def download_img(True_url_list, name_list):
    for i in range(len(name_list)):
        True_url = True_url_list[i]
        name = name_list[i]
        urllib.request.urlretrieve(url=True_url, filename='./站长素材的小猫图片/' + name + '.jpg')


# 建立程序入口
def main():
    start_page = int(input("请输入开始页码:"))
    end_page = int(input("请输入结束页码:"))
    for page in range(start_page, end_page + 1):
        request = create_request(page)
        content = get_content(request)
        name_list = get_name(content)
        url_list = get_links(content)
        True_url_list = get_img_urls(url_list)
        download_img(True_url_list, name_list)


if __name__ == '__main__':
    main()
