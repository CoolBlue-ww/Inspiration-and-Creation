import urllib.request

url = 'https://www.baidu.com'
response = urllib.request.urlopen(url)
# 一个类型六个方法
# print(type(response))  response是HTTPResponse类型

# content = response.read(3) read的里面的数字是读几个字节

# content = response.readline() 读取一行

# content = response.readlines()  一行一行读

# print(response.getcode())  返回状态码，200，404，500

# print(response.geturl())  返回url地址

# print(response.getheaders())  获取一些状态信息

# 一个类型HTTPResponse
# 六个方法：read,readlin,readlines,(getcode,geturl,getheaders).
