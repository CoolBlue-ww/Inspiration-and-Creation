import urllib.request

url = 'https://www.baidu.com'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/132.0.0.0'
                  'Safari/537.36 Edg/132.0.0.0'
}

request = urllib.request.Request(url=url, headers=headers)

# handler build_opener open
handler = urllib.request.HTTPHandler()  # 获取handler对象
opener = urllib.reuqest.build_opener(handler)  # 获取opener对象
response = opener.open(request)  # 调用open方法

# response = urllib.request.urlopen(request)

content = response.read().decode('utf-8')

print(content)
