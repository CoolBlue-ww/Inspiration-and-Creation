import requests
from lxml import etree
import json


def get_url(url):
    response = requests.get(url)
    content = response.text
    tree = etree.HTML(content)
    a_list = tree.xpath('//a/@href')
    url_list = []
    if a_list:
        for a in a_list:
            if 'https' not in a and a[:2] == '//':
                url = 'https:' + a
                url_list.append(url)
            if 'https' not in a and len(a) >= 2 and a[0] == '/' and a[1] != '/':
                url = 'https://www.stats.gov.cn' + a
                url_list.append(url)
            if 'https' not in a and len(a) >= 2 and a[0] != '/' and a[1] != '/':
                url = 'https://www.stats.gov.cn/' + a
                url_list.append(url)
            if 'https://' in a:
                url_list.append(a)
    else:
        pass
    js = tree.xpath('//script/@src')
    if js:
        for j in js:
            if 'https://' in js:
                url_list.append(j)
            elif len(j) >= 2 and j[0] == '/' and j[1] != '/':
                url = 'https://www.stats.gov.cn' + j
                url_list.append(url)
            if len(j) >= 2 and j[0] != '/' and j[1] != '/':
                url = 'https://www.stats.gov.cn/' + j
                url_list.append(url)
    else:
        pass

    t = tree.xpath('//img/@src')
    t_ = tree.xpath('//img/@data-original')
    if t or t_:
        for tt in t + t_:
            if 'https://' in js:
                url_list.append(tt)
            elif len(tt) >= 2 and tt[0] == '/' and tt[1] != '/':
                url = 'https://www.stats.gov.cn' + tt
                url_list.append(url)
            if len(tt) >= 2 and tt[0] != '/' and tt[1] != '/':
                url = 'https://www.stats.gov.cn/' + tt
                url_list.append(url)
    else:
        pass
    return url_list


# base_urls = [f"https://sc.chinaz.com/ppt/index_{num}.html" for num in range(2, 3, 1)]
base_urls = ['https://news.163.com/college']
# total_url_list = []
# for base_url in base_urls:
#     url_list = get_url(base_url)
#     total_url_list += url_list
# pp = set(total_url_list)
# pp_ = list(pp)
# print(pp_)


# response = requests.get(base_urls[0])
# content = response.text
# tree = etree.HTML(content)
# a_list = tree.xpath('//a/@href')
# # print(a_list)
# ss = []
# for i in a_list:
#     if 'http' in i:
#         ss.append(i)
#     else:
#         continue
# qq = set(ss)
# print(qq)


from parse import result

tasks = [{'data': {'url': url}} for url in result]

with open('urls_.json', 'a') as file:
    json.dump(tasks, file, indent=4)
