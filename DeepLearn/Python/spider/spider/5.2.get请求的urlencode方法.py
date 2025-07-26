# 多个参数
import urllib.request
import urllib.parse

base_url = 'https://www.baidu.com/s?'

data = {
    'wd': '周杰伦',
    'sex': '男',
    'location': '中国台湾'
}

new_data = urllib.parse.urlencode(data)

url = base_url + new_data

# 请求对象的定制
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 '
                  'Safari/537.36 Edg/132.0.0.0'
}

# 制定request对象
request = urllib.request.Request(url=url, headers=headers)

# 向网页发送请求
response = urllib.request.urlopen(request)
# 获取响应的数据
content = response.read().decode('utf-8')
print(content)

