from scrapy import cmdline

spider_name = input("请输入爬虫文件的名字：")
cmdline.execute(['scrapy', 'crawl', str(spider_name)])
