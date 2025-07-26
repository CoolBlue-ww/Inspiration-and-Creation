from bs4 import BeautifulSoup

# 通过解析本地文件来了解bs4的语法
# 默认打开文件的编码是gbk
soup = BeautifulSoup(open('18.解析bs4的基本使用.html', 'r', encoding='utf-8'), 'lxml')
# print(soup)


# 根据标签名查找节点
# 找到的是第一个符合条件的数
# print(soup.a)
# print(soup.a.attrs)  # 获取标签的属性和属性值


# bs4的一些函数
# (1)find
# 返回第一个符合条件的数据
# print(soup.find('a'))

# 根据title的值找到a标签
# print(soup.find('a', title='666'))
# print(soup.find('li', class_='zhangsan'))


# (2)find_all
# 如果是多个数据则需要写入列表
# print(soup.find_all(['a', 'span']))

# limit查找前几个数据
# print(soup.find_all('li', limit=2))


# (3)select
# select返回的是一个列表并且会返回多个数据
# print(soup.select('a'))  # 根据标签

# 可以通过.代表class，类选择器
# print(soup.select('.zhangsan'))

# 可以通过id来查找
# print(soup.select('#hello'))

# 属性选择器
# print(soup.select('li[class]'))
# print(soup.select('a[title]'))
# print(soup.select('a[download]'))


# 层级选择器
# 后代选择器
# print(soup.select('div ul li'))

# 子代选择器
# 某标签的第一级子标签
# print(soup.select('div > ul > li'))


# 找到a标签和li标签的所有对象
# print(soup.select('a, li'))



# 节点信息
#      获取节点内容
# 如果标签中只有内容string和get_text()都可。如果里面还有标签string就不行‘
# obj = soup.select('#d1')[0]
# print(obj.string)
# print(obj.get_text())

# 节点的属性
# obj = soup.select('#xld')[0]
# print(obj.name)  # 标签的名字
# 将属性值作为一个字典返回
# print(obj.attrs)

# 获取节点的属性
obj = soup.select('#xld')[0]
print(obj.attrs.get('id'))
print(obj.get('id'))
print(obj['id'])