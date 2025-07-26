import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
url = 'https://www.zhipin.com/chengshi/c101250300/?'
import time
# data = {
#     'seoRefer': 'index'
# }
#
# headers = {
#     "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
#     "accept-encoding": "gzip, deflate, br, zstd",
#     "accept-language": "zh-CN,zh;q=0.9,en;q=0.8",
#     "cache-control": "max-age=0",
#     # "cookie": "ab_guid=3446c333-d4fc-4f5a-8e3b-a7840ca2f1d4; __zp_stoken__=b34dfw49yGQhBYx4MWAtbw45Jc8KCeH9Vw4JzWkjDhUbCs8K%2BVcOEwr9IRlV5wr1VwppSw4VZwopuwoZQwpp%2Bw4LCpcSOwp%2FDr0vCm2LCn8Sfw7LFgMW0YcSCwr%2FCnEMtDxURFAYSFBAVExAGDQgKCwkNCAoMCh4HCUIrxIPCmhJARU5CMl5ITBBeXW5TW1ITZFRPQEFaYRNjQSlDQkBFw4XDnMOFB8K7P8OAEsK6RcOEY0I4RT%2FDgsKeMzMdD8ODfBHCv8KHBsOAw7MTw4PCkBTDlVjDtMOaGMOFxI4nRDbDhcWATkMiOzZCOUVAN0JDMkB7w5NZw6%2FDnRfDg8OoNUUWOkNFN0RCQ0U5NjwvRT1WNENANToMBwkLFDE4w4TCrcK%2Fw5tDRQ%3D%3D; lastCity=101250300; __l=r=https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DuMS3cRaKqpg7D0Cl3P1Q4bdfGWpU4Y7jry1G8JKF4okSlMYuwyauvsI-Z6Zw2H5i%26wd%3D%26eqid%3D85d94f8c003259cb0000000567cffbcf&l=%2F&s=1; __g=-; Hm_lvt_194df3105ad7148dcf2b98a91b5e727a=1741676564,1741683672; HMACCOUNT=F718ACC2443D0B04; __zp_seo_uuid__=fc83e5df-80d5-433f-8165-f4c1dbf5cd0e; __c=1741683671; __a=78760799.1741676565.1741676565.1741683671.21.2.5.21; Hm_lpvt_194df3105ad7148dcf2b98a91b5e727a=1741683877",
#     "priority": "u=0, i",
#     "referer": "https://www.zhipin.com/",
#     "sec-ch-ua": "\"Chromium\";v=\"134\", \"Not:A-Brand\";v=\"24\", \"Google Chrome\";v=\"134\"",
#     "sec-ch-ua-mobile": "?0",
#     "sec-ch-ua-platform": "\"Windows\"",
#     "sec-fetch-dest": "document",
#     "sec-fetch-mode": "navigate",
#     "sec-fetch-site": "same-origin",
#     "sec-fetch-user": "?1",
#     "upgrade-insecure-requests": "1",
#     "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36"
# }
#
# response = requests.get(url=url, headers=headers, params=data)
#
# content = response.text
#
# cookies = response.cookies.get_dict().items()
# print(cookies)
# print(content)
path = 'chromedriver.exe'
service = Service(path)
browser = webdriver.Chrome(service=service)
browser.get(url)
time.sleep(6)
cookies = browser.get_cookies()

print(cookies)
input()