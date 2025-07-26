import requests
from lxml import etree

url = 'https://www.hongxiu.com/book/18899519001291804#Catalog'
# url = 'https://www.hongxiu.com/book/29761858904035708#Catalog'

def get_link():
    code = requests.get(url).text
    html = etree.HTML(code)
    link = html.xpath('//div[@class="volume"]/ul[@class="cf"]/li/a')
    return link

def download(link):
    body_url = 'https://www.hongxiu.com/{}'.format(link)
    code = requests.get(body_url).text
    html = etree.HTML(code)
    title = html.xpath('//h1[@class="j_chapterName"]/text()')[0]
    p_list = html.xpath('//div[@class="ywskythunderfont"]/p')
    with open('book/%s.txt' % title, 'w', encoding='utf-8') as f:
        for p in p_list:
            content = p.xpath('./text()')[0]
            f.write(content + '\n')
    print('{}.txt 下载成功.'.format(title))

def main():
    link = get_link()
    for l in link:
        href = l.xpath('./@href')[0]
        download(href)

if __name__ == '__main__':
    main()
