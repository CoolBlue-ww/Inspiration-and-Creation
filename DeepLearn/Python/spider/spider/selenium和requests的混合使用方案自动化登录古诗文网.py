from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random
import requests
from bs4 import BeautifulSoup
import pytesseract
from PIL import Image, ImageEnhance, ImageFilter
from bs4 import BeautifulSoup
from requests.cookies import create_cookie


# 封装一个函数用来切换窗口句柄
def switch_window(browser):
    all_windows = browser.window_handles
    browser.switch_to.window(all_windows[-1])
    return


# 封装一个函数用来轻微滚动页面
def rolling_page(browser):
    js_button = 'document.documentElement.scrollTop=300'
    browser.execute_script(js_button)
    return


# 封装一个函数用来初始化浏览器实例
def create_browser():
    path = 'chromedriver.exe'
    service = Service(path)
    browser = webdriver.Chrome(service=service)
    return browser


# 封装一个函数用来自动识别登录页面的验证码
def img_text(img_path):
    # 读取文件
    image = Image.open(img_path)
    # 灰质化
    image = image.convert('L')
    image = ImageEnhance.Contrast(image).enhance(2)
    image = image.filter(ImageFilter.MedianFilter(size=3))
    # 读取，识别验证码内容
    captcha_text = pytesseract.image_to_string(image, config='--psm 6 --oem 3')
    data_text = captcha_text.strip()
    return data_text


# 封装一个函数进行随机延迟
def delay_sleep():
    delay = random.uniform(1.5, 2.5)
    time.sleep(delay)
    return


# 封装一个函数用来进入目标页面
def enter_page(browser):
    browser.get('https://www.baidu.com')
    # 随机延迟，模拟用户等待页面加载完成。
    delay_sleep()
    # 向文本框输入搜索内容
    text_box = browser.find_element(By.ID, 'kw')
    text_box.send_keys('古诗文网')
    # 显像等待
    condition = EC.element_to_be_clickable((By.ID, 'su'))
    button1 = WebDriverWait(browser, 10).until(condition)
    button1.click()
    # 随机延迟，模拟用户在寻找目标内容。
    delay_sleep()
    gushiwen = browser.find_element(By.LINK_TEXT, '古诗文网-古诗文经典传承')
    gushiwen.click()
    '''此时进入古诗文网官网，需要切换窗口句柄。'''
    switch_window(browser)
    # 随机延迟，模拟用户在寻找自己感兴趣的内容（这里假设用户想要去看李白的生平简介）。
    delay_sleep()
    condition = EC.element_to_be_clickable((By.LINK_TEXT, '作者'))
    button2 = WebDriverWait(browser, 10).until(condition)
    button2.click()
    # 进入李白的页面介绍
    button3 = browser.find_element(By.XPATH, '//div[@id="leftZhankai"]/div/div/p/a/b[1]')
    button3.click()
    # 随机延迟并且切换窗口句柄
    delay_sleep()
    switch_window(browser)
    '''假如这时用向下滑动，对李白的轶事典故感兴趣。但是需要点击展开，这时自动跳转到登录页面，引导用户登录后查看。'''
    # 模拟滚动
    rolling_page(browser)
    # 点击展开进入登录页面
    button4 = browser.find_element(By.XPATH, '//div/div[@id="fanyi536"]/div/div/a')
    button4.click()
    # 中断三秒，获取当前页面的url地址和当前页面的所有cookie。
    time.sleep(3)
    denglu_url = browser.current_url
    cookies = browser.get_cookies()
    # 保持浏览器始终为打开状态，防止某些cookie因为浏览器的关闭而失效。
    return denglu_url, cookies


# 封装一个函数,用来提交表单发送post请求来模拟登录.
def login_page(browser, denglu_url, cookies):
    # 建立一个session会话对象.
    session = requests.session()
    """
    这里需要将浏览器的cookie注入session对象,让后续的请求继承此时真实浏览器的状态.
    """
    for cookie_data in cookies:
        # 创建一个完整的 cookie 对象
        cookie = create_cookie(
            name=cookie_data["name"],
            value=cookie_data["value"],
            domain=cookie_data.get("domain"),  # 可选属性
            path=cookie_data.get("path", "/"),  # 默认为 "/"
            expires=cookie_data.get("expires"),  # 可选属性
            secure=cookie_data.get("secure", False),  # 默认为 False
            rest={"HttpOnly": cookie_data.get("httpOnly")}  # 其他属性
        )
        session.cookies.set_cookie(cookie)
    '''此后需要再一次向登录页面发送get请求,以完成对浏览器的衔接.并且获取网页中的隐藏域和验证码信息.'''
    # 请求头必须要和浏览器的请求头高度一致.
    headers = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        # "accept-encoding": "gzip, deflate, br, zstd",
        "accept-language": "zh-CN,zh;q=0.9",
        "priority": "u=0, i",
        "referer": "https://www.gushiwen.cn/authorv_b90660e3e492.aspx",
        "sec-ch-ua": "\"Not(A:Brand\";v=\"99\", \"Google Chrome\";v=\"133\", \"Chromium\";v=\"133\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "document",
        "sec-fetch-mode": "navigate",
        "sec-fetch-site": "same-origin",
        "upgrade-insecure-requests": "1",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36"
    }
    # 获取网页的HTML源码
    response = session.get(url=denglu_url, headers=headers)
    content = response.text
    # 利用beautifulsoup来解析查找网页内容.
    # 获取页面中的隐藏域信息
    soup = BeautifulSoup(content, 'lxml')
    viewstate = soup.select('#__VIEWSTATE')[0]['value']
    viewstategenerator = soup.select('#__VIEWSTATEGENERATOR')[0]['value']
    # 获取网页中的验证码信息
    img_url = 'https://www.gushiwen.cn' + soup.select('#imgCode')[0]['src']
    img_response = session.get(url=img_url)
    # 将验证码下载到本地,实现桥梁的目的.再同tesseract引擎去识别验证码.
    with open('img_data.jpg', 'wb') as fb:
        fb.write(img_response.content)
    # 调用img_text函数进行识别.
    img_path = 'img_data.jpg'
    code = img_text(img_path)
    '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~手动分割线~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
    # 传递参数
    data = {
        "__VIEWSTATE": viewstate,
        "__VIEWSTATEGENERATOR": viewstategenerator,
        "from": "http://www.gushiwen.cn/user/collect.aspx",
        "email": "3520352176@qq.com",
        "pwd": "COOKIE",
        "code": code,
        "denglu": "登录"
    }
    # 抓取网页源码中form标签的action属性,以此来获取表单的提交地址.
    action = soup.select('#aspnetForm')[0].attrs.get('action')
    # 利用字符串的切片去除返回属性的无用符号
    action = action[1::1]
    # 再利用字符串拼接，得到完整的表单提交地址
    form_url = 'https://www.gushiwen.cn/user' + action
    # 模拟登录,提交表单.
    response = session.post(url=form_url, data=data, headers=headers)
    if response.status_code == 200:
        print('已经成功发送请求,获得服务器的响应!')
    else:
        print('发送请求失败,验证码识别错误.即将重新发送请求!')
        login_page(browser, denglu_url, cookies)
    # 再获取post请求的coolie.并且把他和浏览器同步.
    post_cookie = session.cookies.get_dict()
    print(post_cookie)
    for name, value in post_cookie.items():
        browser.add_cookie({
            'name': name,
            'value': value,
            'domain': 'www.gushiwen.cn',
            'path': '/',
            'secure': False
        })
    # 刷新页面后点击,进入登录状态
    browser.refresh()
    time.sleep(4)
    button = browser.find_element(By.LINK_TEXT, '我的')
    button.click()
    input('已经成功完成登录！')
    input()
    # 回到前面的网页查看内容
    browser.back()
    browser.back()
    # 欣赏完整的轶事典故
    input()


# 封装主函数，建立程序入口。
def main():
    browser = create_browser()
    denglu_url, cookies = enter_page(browser)
    login_page(browser, denglu_url, cookies)


if __name__ == '__main__':
    main()
