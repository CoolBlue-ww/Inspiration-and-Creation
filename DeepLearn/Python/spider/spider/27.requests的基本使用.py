import requests

url = 'https://www.baidu.com'

response = requests.get(url)


# 一个类型六个属性
print(type(response))


# 设置响应的编码格式
response.encoding = 'utf-8'

# 获取网页源码
print(response.text)

# 返回一个url地址
print(response.url)

# 获取网页二进制数据
print(response.content)

# 获取状态码
print(response.status_code)

# 获取响应头
print(response.headers)
