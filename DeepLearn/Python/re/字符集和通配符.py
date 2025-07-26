import re
import urllib.request
import pymysql
import time
import random
import urllib.error
import os

# 爬取站长素材图片
class DownloadImage:
    # 创建init方法
    def __init__(self):
        print('A:风景图片,B:动物图片,C:美食图片,D:人物图片,E:抽象图片,F:民族艺术,G:建筑图片,H:装修图片')
        print('I:科技交通,J:体育图片,K:其他图片,L:生活用品,M:太空科学,N:花草图片,O:水资源')
        self.picture_name = input('请选择您要下载的图片类型:')
        # 建立一部字典用来映射，选项的中文拼音。
        self.picture_dict = {
            'A': 'fengjing',
            'B': 'dongwutupian',
            'C': 'meishitupian',
            'D': 'renwutupian',
            'E': 'chouxiangtupian',
            'F': 'minzuyishutupian',
            'G': 'jianzhutupian',
            'H': 'zhuangxiutupian',
            'I': 'kejijiaotongtupian',
            'J': 'tiyutupian',
            'K': 'qitatupian',
            'L': 'shenghuoyongpintupian',
            'M': 'taikongkexuetupian',
            'N': 'huacaotupian',
            'O': 'shuiziyuantupian',
        }
        # 检测储存下载图片的文件夹是否存在如果不存在将自动创建。
        project_path = f'{self.picture_dict[self.picture_name]}'
        if not os.path.exists(project_path):
            print('指定路径的文件夹不存在!')
            print('正在创建与图片类型相匹配的文件夹......')
            os.makedirs(project_path, exist_ok=True)
            print(f'一个名为{project_path}的文件夹，已在与此脚本同级目录的某个角落创建！！！')
        else:
            print(f'{project_path}文件夹已存在！')
        self.base_url = f'https://sc.chinaz.com/tupian/{self.picture_dict[self.picture_name]}_'
        self.start_url = f'https://sc.chinaz.com/tupian/{self.picture_dict[self.picture_name]}.html'
        self.headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/135.0.0.0 Safari/537.36"
        }

        self.content = self.get_start_content()
        self.page_max = self.get_next_page()
        self.page_num = 1
        while self.page_num <= int(self.page_max):
            if self.page_num == 1:
                print(f'开始下载第{self.page_num}页图片！')
                self.url = self.start_url
                self.content_ = self.get_next_content()
                self.download()
                print(f"第{self.page_num}页已经下载完成！即将准备下载下一页图片！")
                self.page_num += 1
            else:
                print(f'开始下载第{self.page_num}页图片！')
                self.url = self.base_url + str(self.page_num) + '.html'
                self.content_ = self.get_next_content()
                self.download()
                print(f"第{self.page_num}页已经下载完成！即将准备下载下一页图片！")
                self.page_num += 1
                # 随机延迟，防止请求过于频繁。
                time.sleep(random.uniform(0.1, 0.3))
        print("已经完成所有的图片下载任务！总计下载图片数量:%d张" % (int(self.page_max) * 40))
        print('即将把下载的数据插入数据库中！')
        self.enter_mysql()
    # 访问初始页面获取网页源码
    def get_start_content(self):
        # 定制请求对象
        request = urllib.request.Request(url=self.start_url, headers=self.headers)
        # 模拟浏览器向服务器发送请求
        response = urllib.request.urlopen(request)
        content = response.read().decode('utf-8')
        return content

    # 获取每一页的网页源码
    def get_next_content(self):
        # 定制请求对象
        request = urllib.request.Request(url=self.url, headers=self.headers)
        # 模拟浏览器向服务器发送请求
        response = urllib.request.urlopen(request)
        content_ = response.read().decode('utf-8')
        return content_

    # 封装一个download函数来下载图片
    def download(self):
        # 正则匹配img标签
        ret = re.findall(r'<img src=".+?">', self.content_, re.S)
        # 去空格  分割字符串
        # strip  split
        # 初始化一部字典，来储存图片名字和其下载地址。
        img_dict = {}
        for img in ret:
            if img.find('alt') == -1:
                continue
            else:
                data_img = img.split('\n')
                img_src = data_img[2].strip().split('"')[1]
                img_name = data_img[4].strip().split('"')[1]
                # 对图片进一步优化处理
                if "_s.jpg" in img_src:
                    img_url = "https:" + img_src[0:-6:1] + ".jpg"
                    img_dict[img_name] = img_url
                else:
                    img_url = "https:" + img_src[0:-6:1] + ".png"
                    img_dict[img_name] = img_url
                    img_dict[img_name] = img_url

        # 将字典转化为可迭代对象
        dict_items = img_dict.items()
        for img_name, img_url in dict_items:
            try:
                # 下载图片到animal文件夹
                urllib.request.urlretrieve(url=img_url,
                                           filename=f'./{self.picture_dict[self.picture_name]}/' + img_name + '.jpg')
                print(f"{img_name}，下载成功!  图片名称及其对应的下载地址:{img_name}-->{img_url}")
            except urllib.error.HTTPError as e:
                print(f'图片网址已失效，或资源已转移！ 请求失败: {e}')
                print('即将跳过此图片，进入下一张图片的下载！')
                print('~' * 200)
                time.sleep(random.uniform(0.5, 1.5))
                continue
        return None

    # 从网页中获取最大页码数，避免人工查看。
    def get_next_page(self):
        # 用正则查找出网页的最大页码数
        ret = re.findall(pattern=r'<b>\d+</b>', string=self.content, flags=re.S)
        # 选出最大的一个页码
        page_max = ret[-1].strip().split('<b>')[-1].split('</b>')[0]
        return page_max

    def enter_mysql(self):
        img_path = f'{self.picture_dict[self.picture_name]}'
        img_name_list = os.listdir(img_path)
        for image_name in img_name_list:
            with open(f'{self.picture_dict[self.picture_name]}/{image_name}', 'rb') as f:
                data = f.read()
            db_config = {
                'host': 'localhost',
                'port': 3306,
                'user': 'root',
                'password': 'CKR_JAVASCRIPT_2005',
                'database': 'image_db',
                'charset': 'utf8'
            }

            try:
                connection = pymysql.connect(**db_config)
                cursor = connection.cursor()

                sql = "INSERT INTO images (image_name, image_data) VALUES (%s, %s)"
                cursor.execute(sql, (image_name, data))

                connection.commit()
                print(f"{image_name}已成功插入到数据库！")
            except pymysql.MySQLError as e:
                print(f"数据库错误:{e}")

                connection.rollback()
            finally:
                if connection:
                    connection.close()


a = DownloadImage()

