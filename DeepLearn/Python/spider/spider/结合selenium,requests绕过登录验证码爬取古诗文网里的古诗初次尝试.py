# 结合selenium,requests,Beautifulsoup,xpath,验证码,完成自动化登录爬取古诗文网里的古诗初次尝试
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random
from lxml import etree
from PIL import Image, ImageEnhance, ImageFilter
import pytesseract
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


# 封装一个函数用来识别获取到的验证码图片
def get_data_text(img_path):
    # 读取文件
    image = Image.open(img_path)
    # 灰质化
    image = image.convert('L')
    image = ImageEnhance.Contrast(image).enhance(2)
    image = image.filter(ImageFilter.MedianFilter(size=3))
    # 读取验证码内容
    captcha_text = pytesseract.image_to_string(image, config='--psm 6 --oem 3')
    data_text = captcha_text.strip()
    return data_text


# 封装一个切换窗口句柄的函数
def switch_window(browser):
    all_windows = browser.window_handles
    browser.switch_to.window(all_windows[-1])
    return


# 封装一个轻微滚动的函数
def page_bottom(browser):
    js_button = 'document.documentElement.scrollTop=250'
    browser.execute_script(js_button)
    return


# 封装一个函数用来初始化浏览器
def create_browser():
    # 配置浏览器选项（允许所有Cookie）
    options = Options()
    options.add_argument("--disable-features=BlockThirdPartyCookies")  # 允许第三方Cookie
    options.add_argument("--disable-extensions")  # 禁用可能干扰Cookie的插件
    path = 'chromedriver.exe'
    service = Service(path)
    browser = webdriver.Chrome(service=service, options=options)
    return browser


# 封装一个逐步进入目标页面的函数
def enter_page(browser):
    browser.get('https://www.baidu.com')
    # 随机延迟
    delay = random.uniform(1.5, 2.5)
    time.sleep(delay)
    # 输入搜索内容
    input_button = browser.find_element(By.ID, 'kw')
    input_button.send_keys('古诗文网')
    # 延迟两秒
    button = browser.find_element(By.ID, 'su')
    button.click()
    # 随机延迟，模拟用户在寻找内容
    condition = EC.element_to_be_clickable((By.LINK_TEXT, '古诗文网'))
    content_button = WebDriverWait(browser, 10).until(condition)
    content_button.click()
    # 切换窗口句柄，此时已经到达“古诗文网”官网
    switch_window(browser)
    # 随机延迟
    time.sleep(delay)
    # 模拟用户对于进入新网站的随机探索，随机点击名句导航进行阅读和欣赏。
    condition = EC.element_to_be_clickable((By.XPATH, '//div/div[@id="zhengwen9211704923ca"]/p/a/b'))
    XIN_button = WebDriverWait(browser, 10).until(condition)
    XIN_button.click()
    # 随机延迟等待页面加载完成
    time.sleep(delay)
    # 随机点击一首名句进行观看
    # mingju_button = browser.find_elements(By.XPATH, '//div/div[contains(@class, "cont")]/a')[3]
    # mingju_button.click()
    # 切换窗口句柄
    switch_window(browser)
    # 随机延迟等待页面加载完成
    time.sleep(delay)
    # 轻微滚动查看译文和注释
    page_bottom(browser)
    # 随机延迟
    time.sleep(delay)
    # 点击展开查看全部内容
    # condition = EC.element_to_be_clickable((By.LINK_TEXT, '展开阅读全文V'))
    # XIN2_button = WebDriverWait(browser, 10).until(condition)
    XIN2_button = browser.find_element(By.XPATH, '//div/div[contains(@id, "fany")]//a')
    XIN2_button.click()
    # 发现查看全部内容需要登录已经自动跳转到登录页面
    switch_window(browser)
    # 随机延迟等待页面加载完毕
    time.sleep(delay)
    # 获取登录页面的页面源码，提取出提交表单的API接口
    page_code = browser.page_source
    # 用bs4查找出form标签里面的action属性
    soup = BeautifulSoup(page_code, 'lxml')
    action = soup.select('#aspnetForm')[0].attrs.get('action')
    # 利用字符串的切片去除返回属性的无用符号
    action = action[1::1]
    # 再利用字符串拼接，得到完整的表单提交地址
    form_url = 'https://www.gushiwen.cn/user' + action
    return form_url, page_code


# 封装一个函数用于模拟登录
# 利用requests的post请求来完成登录
def login(form_url, page_code, browser):
    # 根据接口的负载信息，准备参数data
    # 获取隐藏域的数据
    soup = BeautifulSoup(page_code, 'lxml')
    viewstate = soup.select('#__VIEWSTATE')[0]['value']
    viewstategenerator = soup.select('#__VIEWSTATEGENERATOR')[0]['value']
    # 获取验证码数据
    img_src = soup.select('#imgCode')[0]['src']
    img_url = 'https://www.gushiwen.cn' + img_src
    # 定制一个session对象
    session = requests.Session()
    img_data = session.get(img_url)
    with open('yanzhengma.png', 'wb') as f:
        f.write(img_data.content)
    # 暂停五秒等待图片下载完成
    time.sleep(5)
    # 指定验证码图片的下载路径
    img_path = 'yanzhengma.png'
    # 接下来用tesseract引擎来识别验证码
    code = get_data_text(img_path)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/133.0.0.0 Safari/537.36'
    }
    data = {
        '__VIEWSTATE': viewstate,
        '__VIEWSTATEGENERATOR': viewstategenerator,
        'from': 'https: // www.gushiwen.cn / shiwenv_501b36c2ddae.aspx',
        'email': '3520352176 @ qq.com',
        'pwd': 'COOKIE',
        'code': code,
        'denglu': '登录'
    }
    response_post = session.post(url=form_url, data=data, headers=headers)
    session.get('https://www.gushiwen.cn/user/collect.aspx', headers=headers)
    session.get('http://www.gushiwen.cn/user/collect.aspx', headers=headers)
    # cookies = response_post.cookies()
    # print(cookies)
    # 清除现有的所有cookie
    browser.get('https://www.gushiwen.cn')
    browser.delete_all_cookies()
    print(browser.current_url)
    # 将所有的cookie和浏览器实例绑定
    for name, value in session.cookies.get_dict().items():
        browser.add_cookie({
            'name': name,
            'value': value,
            'domain': 'www.gushiwen.cn',
            'path': '/',
            'secure': True
        })
    browser.refresh()
    browser.get("http://www.gushiwen.cn/user/collect.aspx")

    # if "dashboard" in browser.current_url:
    #     print('已成功进入页面')
    # else:
    #     print('还是不行')
    # return


# 封装一个主函数
def main():
    browser = create_browser()
    form_url, page_code = enter_page(browser)
    print(page_code)
    # login(form_url, page_code, browser)
    # # 随机延迟等待登录完成后用户界面的刷新
    # delay = random.uniform(1.5, 2.5)
    # time.sleep(delay)
    # # 返回上一个窗口，浏览需要登录的赏析部分
    # # browser.back()
    # switch_window(browser)
    # time.sleep(30)


if __name__ == '__main__':
    main()
