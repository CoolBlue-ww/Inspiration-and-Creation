import urllib.request
from lxml import etree


# 请求对象的定制
# https://sc.chinaz.com/tag_tupian/omeimeinu.html
# https://sc.chinaz.com/tag_tupian/omeimeinu_2.html
def create_request(page):
    if page == 1:
        url = 'https://sc.chinaz.com/tag_tupian/omeimeinu.html'
    else:
        url = 'https://sc.chinaz.com/tag_tupian/omeimeinu_' + str(page) + '.html'
    # 请求头
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/133.0.0.0'
                      'Safari/537.36'
    }
    # 请求对象的定制
    request = urllib.request.Request(url=url, headers=headers)
    return request


# 获取服务器响应的数据
def get_content(request):
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')
    return content


# 下载
def down_load(content):
    # 解析，查找有用的数据并下载
    tree = etree.HTML(content)
    src_list = tree.xpath('//div[contains(@class, "小猫图片-list com-img-txt-list masonry")]//img/@src')
    name_list = tree.xpath('//div[contains(@class, "小猫图片-list com-img-txt-list masonry")]//img/@alt')

    for i in range(len(src_list)):
        name = name_list[i]
        src = src_list[i]
        URL = 'https' + src
        urllib.request.urlretrieve(url=URL, filename='./15解析站长素材/' + name + '.jpg')


# 建立主函数
def main():
    start_page = int(input('请输入起始页码：'))
    end_page = int(input('请输入结束页码：'))
    for page in range(start_page, end_page + 1):
        # 请求对象的定制
        request = create_request(page)
        # 获取网页的内容
        content = get_content(request)
        # 下载
        down_load(content)


# 建立程序的入口
if __name__ == '__main__':
    main()
