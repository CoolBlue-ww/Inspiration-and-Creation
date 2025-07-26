from lxml import etree

# xpath
# （1）本地文件  etree.parse
# （2）服务器响应的数据   etree.HTML

tree = etree.parse('13本地.html')

# print(tree)
# xpath路径查询
# li_list = tree.xpath('//ul/li')


# print(type(li_list))
# 查找所有有id属性的标签
# li_list = tree.xpath('//ul/li[@id]/text()')
# 查找属性id=11的li标签
# li_list = tree.xpath('//ul/li[@id="11"]/text()')

# 查找id为11的li标签的class属性值
# li = tree.xpath('//ul/li[@id="11"]/@class')
#
# print(li)

# 模糊查询
# li_list = tree.xpath('//ul/li[contains(@id, "c")]/text()')

# li_list = tree.xpath('//ul/li[starts-with(@class, "cnmd")]/text()')

# 查询id=11和class=cnmd的li
# li_list = tree.xpath('//ul/li[@id="11" and @class="cnmd"]/text()')

# 或
li_list = tree.xpath('//ul/li[@id="11"]/text()  | //ul/li[@class="cnmd"]/text()')
print(li_list)
print(len(li_list))