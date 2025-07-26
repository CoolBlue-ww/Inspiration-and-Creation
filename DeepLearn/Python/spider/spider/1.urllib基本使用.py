import urllib.request

# 定义一个网址
url = 'https://www.toutiao.com'
# 模拟浏览器向服务器发送请求
response = urllib.request.urlopen(url)  # 响应里包括了页面源码之外的其他数据
# 获取响应中的页面源码
content = response.read().decode('utf-8')  # read方法反应的是二进制的数据，需要decode方法解码
print(content)