import jsonpath
import json

obj = json.load(open('16.解析jsonpath.json', 'r', encoding='utf-8'))
# print(obj)

# 说有书的作者
# author_list = jsonpath.jsonpath(obj, '$.store.book[*].author')
# print(author_list)

# 所有作者
# author_list = jsonpath.jsonpath(obj, '$..author')
# print(author_list)

# store下面的所有元素
# tag_list = jsonpath.jsonpath(obj, '$.store.*')
# print(tag_list)

# store里面所有东西的price
# price_list = jsonpath.jsonpath(obj, '$.store..price')
# print(price_list)

# 第三个书
# book = jsonpath.jsonpath(obj, '$..book[2]')
# print(book)

# 最后一本书
# last_book = jsonpath.jsonpath(obj, '$..book[(@.length-1)]')
# print(last_book)

# 前两本书
# book_list = jsonpath.jsonpath(obj, '$..book[0,1]')
# print(book_list)
# book_list = jsonpath.jsonpath(obj, '$..book[:2]')
# print(book_list)

# 过滤出所有包含isbn的书
# 条件过滤需要在（）前面增加一个？
# book_list = jsonpath.jsonpath(obj, '$..book[?(@.isbn)]')
# print(book_list)

# 哪本书超过了十块钱
book_list = jsonpath.jsonpath(obj, '$..book[?(@.price>10)]')
print(book_list)