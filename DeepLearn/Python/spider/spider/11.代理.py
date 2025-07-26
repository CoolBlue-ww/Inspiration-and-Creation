import urllib.request

url = 'http://www.baidu.com/s?wd=ip'

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/132.0.0.0'
                  'Safari/537.36 Edg/132.0.0.0'
}
proxies = {
    'http': '42.48.10.122:8080'
}

request = urllib.request.Request(url=url, headers=headers)

handler = urllib.request.ProxyHandler(proxies=proxies)

opener = urllib.request.build_opener(handler)

response = opener.open(request)
# response = urllib.request.urlopen(request)

content = response.read().decode('utf-8')

with open('ip.html', 'w', encoding='utf-8') as fb:
    fb.write(content)