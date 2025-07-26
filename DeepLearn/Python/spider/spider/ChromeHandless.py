from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def chromehandless():
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # 启用无头模式
    chrome_options.add_argument("--disable-gpu")  # 禁用 GPU 加速（可选）
    chrome_options.add_argument("--no-sandbox")  # 禁用沙盒模式（可选）
    chrome_options.add_argument("--disable-dev-shm-usage")  # 禁用共享内存（可选）

    path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
    chrome_options.binary_location = path

    browser = webdriver.Chrome(options=chrome_options)

    # browser.get('https://www.baidu.com')
    #
    # content = browser.page_source
    # print(content)
    #
    # browser.save_screenshot('baidu.png')
    return browser
