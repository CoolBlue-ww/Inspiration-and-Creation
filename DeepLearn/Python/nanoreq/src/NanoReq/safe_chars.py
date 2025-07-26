import string
import random
import idna
import json

"""
十六进制数
"""
hex_num = [f"%{num:02X}" for num in range(256)]

'''通用分割符'''
gen_delims = [":", "/", "?", "#", "[", "]", "@"]
'''子分割符'''
sub_delims = ["!", "$", "&", "'", "(", ")", "*", "+", ",", ";", "="]
'''保留符号'''
reserved = gen_delims + sub_delims

alpha = string.ascii_lowercase + string.ascii_uppercase
digit = string.digits

'''无保留字符'''
unreserved = [*alpha, *digit, "-", "_", ".", "~"]

unreserved_ = ["a-z", "A-Z", "0-9", "-", "_", ".", "~"]


"""
方案的字符
"""
scheme = [*alpha, *digit, "+", "-", "."]

scheme_ = ["a-z", "A-Z", "0-9", "+", "-", "."]

"""
用户信息的字符
"""
userinfo = [*unreserved, *random.choices(hex_num, k=5), *sub_delims, ":"]

userinfo_ = ["a-z", "A-Z", "0-9", '%hex', "-", "_", ".", "~", ":", "!", "$", "&", "'", "(", ")", "*", "+", ",", ";", "="]


"""
主机的字符
"""
# host = ['IP-literal', 'IPv4address', 'reg-name']

"""
域名的字符
"""
host = [*alpha, *digit, '-', '.']

host_ = ["a-z", "A-Z", "0-9", '-', '.']

"""
IP的字符
"""
IPv4 = [*digit, "."]

IPv4_ = ["0-9", "."]

IPv6 = [*digit, *alpha, "[", "]", ":"]

Ipv6 = ["a-z", "A-Z", "0-9", "[", "]", ":"]

IP_literal = [*IPv6, "."]

IP_literal_ = ["a-z", "A-Z", "0-9", "[", "]", ":", "."]

"""
端口号的字符
"""
port = [*digit]

port_ = ["0-9"]

"""
权威的字符
"""
authrity = (*[*userinfo, "@"], *host, *[":", *port])

authrity_ = ["a-z", "A-Z", "0-9", '%hex', "-", "_", ".", "~", ":", "!", "$", "&", "'", "(", ")", "*", "+", ",", ";", "=", "@", ":"]


"""
路径的字符
"""
pchar = [*unreserved, *random.choices(hex_num, k=5), *sub_delims, ":", "@"]

pchar_ = ["%hex", "a-z", "A-Z", "0-9", "-", "_", ".", "~", "!", "$", "&", "'", "(", ")", "*", "+", ",", ";", "=", ":", "@"]

"""
查询符号
"""
query = [*pchar, "/", "?"]

query_ = ["%hex", "a-z", "A-Z", "0-9", "-", "_", ".", "~", "!", "$", "&", "'", "(", ")", "*", "+", ",", ";", "=", ":", "@", "/", "?"]

"""
碎片的符号
"""
fragment = [*pchar, "/", "?"]

fragment_ = ["%hex", "a-z", "A-Z", "0-9", "-", "_", ".", "~", "!", "$", "&", "'", "(", ")", "*", "+", ",", ";", "=", ":", "@", "/", "?"]

common_scheme = [
    "http", "https", "ftp", "file",
    "mailto", "data", "javascript",
    "ws", "wss", "nfs", "smb", "webdav",
    "sftp", "ssh", "scp",
]

common_tld = [
    "com", "org", "net", "edu", "gov", "mil", "int", "arpa", "biz", "info", "name", "pro", "aero", "coop", "museum",
    "ac", "ad", "ae", "af", "ag", "ai", "al", "am", "an", "ao", "aq", "ar", "as", "at", "au", "aw", "ax", "az", "ba",
    "bb", "bd", "be", "bf", "bg", "bh", "bi", "bj", "cn"]

punycode = [
    "xn--", "xn--0zwm56d", "xn--3e0b707e", "xn--3hcrj9c", "xn--45brj9c", "xn--45brj9c", "xn--80akhbyknj4f",
    "xn--90a3ac", "xn--90ais", "xn--clchc0ea0b2g2a9gcd", "xn--d1alf", "xn--e1a4c", "xn--fiqs8s", "xn--fiqz9s",
    "xn--fpcrj9c3d", "xn--fzc2c9e2c", "xn--gecrj9c", "xn--h2breg3eve", "xn--h2brj9c", "xn--h2brj9c", "xn--j1amh",
    "xn--j6w193g", "xn--kprw13d", "xn--kpry57d", "xn--l1acc", "xn--lgbbat1ad8j", "xn--mgb9awbf",
    "xn--mgba3a4f16a", "xn--mgbaam7a8h", "xn--mgbai9azgqp6j", "xn--mgbayh7gpa", "xn--mgbbh1a", "xn--mgbbh1a71e",
    "xn--mgbc0a9azcg", "xn--mgberp4a5d4ar", "xn--mgbgu82a", "xn--mgbpl2fh", "xn--mgbx4cd0ab", "xn--node",
    "xn--p1ai", "xn--pgbs0dh", "xn--wgbh1c", "xn--wgbl6a", "xn--xkc2al3hye2a", "xn--xkc2dl3a5ee0h", "xn--yfro4i67o",
    "xn--ygbi2ammx",
    "xn--zfr164b",
    "xn--z1a", "xn--z1a2a", "xn--zckzah", "xn--zwf694b", "xn--c1avg", "xn--c2br7g", "xn--cck2b3b", "xn--cck2b3d",
    "xn--mgbc0a9azcg", "xn--mgberp4a5d4ar", "xn--mgbgu82a", "xn--mgbpl2fh", "xn--mgbx4cd0ab",
    "xn--0zwm56d", "xn--3e0b707e", "xn--3hcrj9c", "xn--45brj9c", "xn--45brj9c", "xn--80akhbyknj4f", "xn--90a3ac",
    "xn--90ais", "xn--clchc0ea0b2g2a9gcd", "xn--d1alf", "xn--e1a4c", "xn--fiqs8s", "xn--fiqz9s", "xn--fpcrj9c3d",
    "xn--fzc2c9e2c", "xn--gecrj9c", "xn--h2breg3eve", "xn--h2brj9c", "xn--h2brj9c", "xn--j1amh", "xn--j6w193g",
    "xn--kprw13d", "xn--kpry57d", "xn--l1acc", "xn--lgbbat1ad8j", "xn--mgb9awbf",
    "xn--mgba3a4f16a", "xn--mgbaam7a8h", "xn--mgbai9azgqp6j", "xn--mgbayh7gpa", "xn--mgbbh1a", "xn--mgbbh1a71e",
    "xn--mgbc0a9azcg", "xn--mgberp4a5d4ar", "xn--mgbgu82a", "xn--mgbpl2fh", "xn--mgbx4cd0ab", "xn--node",
    "xn--p1ai", "xn--pgbs0dh", "xn--wgbh1c", "xn--wgbl6a", "xn--xkc2al3hye2a", "xn--xkc2dl3a5ee0h", "xn--yfro4i67o",
    "xn--ygbi2ammx",
    "xn--zfr164b",
    "xn--z1a", "xn--z1a2a", "xn--zckzah", "xn--zwf694",
    "xn--0zwm56d", "xn--3e0b707e", "xn--3hcrj9c", "xn--45brj9c", "xn--45brj9c", "xn--80akhbyknj4f", "xn--90a3ac",
    "xn--90ais", "xn--clchc0ea0b2g2a9gcd", "xn--d1alf", "xn--e1a4c", "xn--fiqs8s", "xn--fiqz9s", "xn--fpcrj9c3d",
    "xn--fzc2c9e2c", "xn--gecrj9c", "xn--h2breg3eve", "xn--h2brj9c", "xn--h2brj9c", "xn--j1amh", "xn--j6w193g",
    "xn--kprw13d", "xn--kpry57d", "xn--l1acc", "xn--lgbbat1ad8j", "xn--mgb9awbf",
    "xn--mgba3a4f16a", "xn--mgbaam7a8h", "xn--mgbai9azgqp6j", "xn--mgbayh7gpa", "xn--mgbbh1a", "xn--mgbbh1a71e",
    "xn--mgbc0a9azcg", "xn--mgberp4a5d4ar", "xn--mgbgu82a", "xn--mgbpl2fh", "xn--mgbx4cd0ab", "xn--node",
    "xn--p1ai", "xn--pgbs0dh", "xn--wgbh1c", "xn--wgbl6a", "xn--xkc2al3hye2a", "xn--xkc2dl3a5ee0h", "xn--y",
    "xn--yfro4i67o", "xn--ygbi2ammx",
    "xn--zfr164b",
]

base64_char = [*alpha, *digit, "+", "/", "="]

common_url = [
    'https://baidu.com',
    'https://chat.deepseek.com/a/chat/s/479b9f10-c769-4366-b8db-21268885d24d',
    'https://gitcode.com/Resource-Bundle-Collection/d54ed#%E6%95%99%E7%A8%8B%E4%BA%AE%E7%82%B9',
    'https://sc.chinaz.com/',
    'https://aspx.sc.chinaz.com/query.aspx?classid=11&keyWord=%E8%80%81%E8%99%8E',
    'https://kimi.moonshot.cn/chat/d02458mf2kq4mi0bigsg',
    'https://leetcode.cn/problems/pascals-triangle/description/',
    'https://tools.liumingye.cn/#google_vignette',
    'https://www.json.cn/encrypt/eval/#google_vignette',
    'https://curlconverter.com/',
    'https://developer.mozilla.org/zh-CN/docs/Web/HTTP/Reference/Methods/GET',
    'https://www.w3school.com.cn/index.html',
    'https://www.sucai999.com/searchlist/lingdaitupian.html',
    'https://cc0.cn/image/dongwu/',
    'https://www.spiderbuf.cn/',
    'https://www.canva.cn/?display-com-option=true%2F',
    'https://www.pexels.com/zh-cn/search/%E8%80%81%E8%99%8E/',
    'https://www.runoob.com/python3/python3-examples.html',
    'https://www.vcg.com/creative-image/shuji/',
    'https://image.baidu.com/search/index?tn=baiduimage&ps=1&ct=201326592&lm=-1&cl=2&nc=1&ie=utf-8&dyTabStr=MCwxMiwzLDEsMiwxMyw3LDYsNSw5&word=%E5%91%A8%E6%9D%B0%E4%BC%A6',
    'https://www.hongxiu.com/category/f1_f1_f1_1_f1_f1_0_1',
    'https://www.runoob.com/cprogramming/c-100-examples.html',
    'https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&wd=%E5%91%A8%E6%9D%B0%E4%BC%A6&fenlei=256&rsv_pq=0xce973393005004c7&rsv_t=cb22UnGFCd4XIovzRBN66IY5Dp92g5w5DuXdnGT8OrywH70zqZ%2Fb14qjlYoX&rqlang=en&rsv_dl=ib&rsv_enter=1&rsv_sug3=18&rsv_sug1=32&rsv_sug7=101',
    'https://fanyi.baidu.com/mtpe-individual/multimodal?query=man%2Cwhat%20can%20i%20say%3F%0A%0A%0A%0A&lang=en2zh#/',
    'https://codebeautify.org/',
    'https://github.com/copilot/c/21d978f8-ab9f-447b-a363-d1e631364675',
    'https://store.steampowered.com/about/',
    'https://store.steamchina.com/',
    'https://www.myfreemp3.com.cn/',
    'https://ollama.com/',
    'https://docs.ultralytics.com/zh/usage/cfg/#train-settings',
    'http://www.kxdaili.com/dailiip.html',
    'https://www.virtualbox.org/',
    'https://support.lenovo.com/us/zc/',
]

# tasks = [{"data": {"url": url}} for url in common_url]
# with open("urls.json", 'w') as f:
#     json.dump(tasks, f, indent=4)
