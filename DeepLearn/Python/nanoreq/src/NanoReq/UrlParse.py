import re
import string


SCHEME = ["http", "https"]

ENCODING = "utf-8"

ERRORS = "strict"

ALL_PERCENT_NUMBER = {'7F', 'ff', '6A', 'Fb', '3b', 'Cb', '6d', '4b', 'c6', '41', 'cF', 'ba', 'AA', 'F3',
                      'ed', 'fe', 'E9', 'a2', 'Ba', 'F8', '2c', 'dc', 'a6', '2e', '2B', '1A', 'db', '6b',
                      '26', 'aC', '34', '7D', '3c', '6B', '4F', 'd5', 'C3', 'a5', '76', 'BC', '18', 'C9',
                      '2f', '4A', 'eC', '5f', '93', 'de', '1d', '4d', '96', 'B7', '4B', 'Bc', 'D1', '3a',
                      '9E', 'd4', '46', '14', 'B8', 'c3', 'd7', '57', '5C', 'ad', '11', 'b3', 'c7', 'BE',
                      'E5', '36', '25', 'C4', 'd2', '1B', '92', '9C', 'A5', 'fA', 'd1', 'e7', 'c8', '4e',
                      'AE', 'Fe', 'C8', 'fa', '97', 'Eb', 'eD', '33', 'DF', 'aa', '9d', 'd6', 'cB', 'A7',
                      '1E', '2F', '69', '6E', '16', '9c', 'ee', '8F', 'CC', '75', 'f6', '5a', '1e', 'e3',
                      'e8', '5b', '7c', '24', '4a', 'C6', 'F4', 'f3', 'FA', '23', '6a', 'Bb', '7A', 'BF',
                      'aF', 'b5', 'd8', 'A3', '78', '3D', 'a9', '2D', '49', 'b6', 'dd', 'Ee', '74', '79',
                      '1D', '47', '35', 'FD', '63', 'Ff', '84', 'eB', '5e', '37', 'Cc', '7E', '9f', '52',
                      'a1', '7f', '58', '68', '28', 'F5', '8b', 'bc', 'c9', '4c', 'DA', 'ef', 'eb', 'fB',
                      'E7', 'E2', 'E3', 'B4', '82', 'FB', '3e', 'E4', '2d', '51', 'B5', 'A6', '99', 'dD',
                      'c4', 'f1', '62', '6C', 'A4', 'Df', '27', '2b', 'd9', 'cC', 'f2', '3B', '5A', 'B2',
                      'dA', 'cf', '5E', '8e', 'C1', '3f', '9a', 'B3', 'Ea', 'AD', 'DC', 'c2', 'Dd', 'bA',
                      'B9', 'Fd', '59', 'CD', 'cd', '81', '38', 'AB', '7C', 'D5', 'CE', 'DD', '64', 'b8',
                      '6e', 'Fc', '17', '3d', '71', '2E', 'Aa', '77', 'Ae', '94', 'D6', '48', 'EE', 'f4',
                      'DB', '61', '6c', '9B', '39', '7a', 'ab', 'fE', 'c5', 'fd', 'da', '13', 'EC', 'f7',
                      '1F', 'C7', '12', '5c', 'a3', '2a', 'a4', 'Cd', 'D2', '9b', 'Ce', '83', 'Ca', '89',
                      'Be', 'Da', '95', 'Cf', 'BD', 'C2', 'Ab', 'dF', '31', '3F', 'Ac', 'Db', 'e5', 'aA',
                      'Af', 'b7', 'EA', '9e', 'e2', '8d', '53', '19', 'Ed', 'fb', 'bf', '66', '7d', '5F',
                      '5D', '5B', 'Fa', '1b', '8D', 'F1', 'e1', 'C5', 'F7', '22', '72', '1a', 'c1', 'a7',
                      'Ef', '44', '5d', '6D', 'e9', 'AC', 'ae', 'Ad', '73', '6f', '4D', 'AF', 'D4', '1f',
                      'A2', '65', 'bC', 'f9', 'FF', '1c', 'dC', 'ec', '54', 'CB', 'A9', 'B1', '86', 'b1',
                      'F9', 'af', 'aE', '32', '67', '87', '8f', 'Ec', 'b2', 'd3', 'dB', '43', 'ce', 'bB',
                      'BA', '8A', '6F', 'CA', 'f5', 'eA', 'bF', '2A', '9F', 'A1', '3A', 'E8', 'De', 'Dc',
                      'ea', '8B', '29', '45', 'aD', 'f8', 'ca', '56', '88', '7B', '7b', 'df', '3C', 'bD',
                      'dE', '3E', 'cc', 'EB', 'bE', 'eE', 'D9', '4f', 'aB', 'Bd', 'CF', 'FC', 'cb', 'fF',
                      'a8', 'bd', 'fD', 'e4', 'be', 'cA', 'FE', 'b4', '8c', 'bb', 'B6', 'e6', '8E', 'EF',
                      '1C', 'BB', '9D', 'fC', 'eF', 'ED', 'fc', 'Bf', '98', 'F6', '91', 'E6', '55', 'DE',
                      '2C', '8a', 'E1', '9A', 'ac', 'cD', '85', 'cE', '7e', 'D8', '4C', '8C', 'A8', 'b9',
                      '4E', 'D3', '21', '15', '42', 'D7', 'F2'}

SPLIT_ONE = {'%3a%2f%2f', ':%2f/', '%3a2F%2f', '%3a2F2F', '%3A2F2F', '%3A/%2f',
             '%3a%2f/', '%3A%2f/', '%3a/2F', '%3A/2F', '%3a//', ':2F/', '%3a%2f2F',
             '%3a2F/', '%3a/%2f', ':/%2f', ':/2F', ':2F2F', '%3A2F%2f', '%3A//',
             ':%2f%2f', '%3A%2f%2f', ':2F%2f', '%3A2F/', '%3A%2f2F', ':%2f2F'}


def gen_delims():
    Gen_Delims = {":", "/", "?", "#", "[", "]", "@"}
    return Gen_Delims


def sub_delims():
    Sub_Delims = {"!", "$", "&", "'", "(", ")", "*", "+", ",", ";", "="}
    return Sub_Delims


def reserved():
    Reserved = {list(gen_delims()) + list(sub_delims())}
    return Reserved


def unreserved():
    Unreserved_i = {"a-z", "A-Z", "0-9"}
    Unreserved_j = {"-", "_", ".", "~"}
    return Unreserved_i, Unreserved_j


def percent():
    Percent_i = {"0-9", "a-f", "A-F"}
    Percent_j = {"%"}
    return Percent_i, Percent_j


def scheme():
    Scheme_i = {"a-z", "A-Z", "0-9"}
    Scheme_j = {"+", "-", "."}
    return Scheme_i, Scheme_j


def userinfo():
    # 可以是百分比编码的字符
    Userinfo_i = {"a-z", "A-Z", "0-9"}  # %hex
    Userinfo_j = {"-", "_", ".", "~", ":", "!", "$", "&", "'", "(", ")", "*", "+", ",", ";", "=", "%"}
    return Userinfo_i, Userinfo_j


def domain_name():
    Domain_Name_i = {"a-z", "A-Z", "0-9"}
    Domain_Name_j = {'-'}
    return Domain_Name_i, Domain_Name_j


def IPv4():
    ipv4 = {"0-9"}
    return ipv4


def IPv6():
    ipv6 = {"a-z", "A-Z", "0-9"}
    return ipv6


def IP_literal():
    ip_literal_i = {"a-z", "A-Z", "0-9"}
    ip_literal_j = {"-", "_", ".", "~", "!", "$", "&", "'", "(", ")", "*", "+", ",", ";", "=", ":"}
    return ip_literal_i, ip_literal_j


def host():
    Host_i = {"a-z", "A-Z", "0-9"}
    Host_j = {"-", "_", ".", "~", "!", "$", "&", "'", "(", ")", "*", "+", ",", ";", "=", ":", "[", "]"}
    return Host_i, Host_j


def port():
    Port = {"0-9"}
    return Port


def authority():
    # 可以是百分比编码的字符
    Authority_i = {"a-z", "A-Z", "0-9"}  # %hex
    Authority_j = {"-", "_", ".", "~", ":", "!", "$", "&", "'", "(", ")", "*", "+", ",", ";", "=", "@", ":", "[", "]",
                   "%"}
    return Authority_i, Authority_j


def pchar():
    # 可以是百分比编码的字符
    Pchar_i = {"a-z", "A-Z", "0-9"}  # %hex
    Pchar_j = {"-", "_", ".", "~", "!", "$", "&", "'", "(", ")", "*", "+", ",", ";", "=", ":", "@", "%"}
    return Pchar_i, Pchar_j


def query():
    # 可以是百分比编码的字符
    Query_i = {"a-z", "A-Z", "0-9"}  # %hex
    Query_j = {"-", "_", ".", "~", "!", "$", "&", "'", "(", ")", "*", "+", ",", ";", "=", ":", "@", "/", "?", "%"}
    return Query_i, Query_j


def fragment():
    # 可以是百分比编码的字符
    Fragment_i = {"a-z", "A-Z", "0-9"}  # %hex
    Fragment_j = {"-", "_", ".", "~", "!", "$", "&", "'", "(", ")", "*", "+", ",", ";", "=", ":", "@", "/", "?", "%"}
    return Fragment_i, Fragment_j


def character_processing():
    authority_i, authority_j = authority()
    pchar_i, pchar_j = pchar()
    query_i, query_j = query()
    fragment_i, fragment_j = fragment()
    au = "".join(list(authority_i) + [re.escape(char) for char in authority_j])
    pc = "".join(list(pchar_i) + [re.escape(char) for char in pchar_j])
    qu = "".join(list(query_i) + [re.escape(char) for char in query_j])
    fr = "".join(list(fragment_i) + [re.escape(char) for char in fragment_j])
    return au, pc, qu, fr


def get_part(url, Mobject):
    URL_PART = {
        "url": url,
        "scheme": Mobject.group(1),
        "authority": Mobject.group(2),
        "path": Mobject.group(3),
        "query": Mobject.group(4),
        "fragment": Mobject.group(5)
    }
    return URL_PART


def inspection_url(url: str or tuple or list or set or dict) -> str or list:
    if isinstance(url, str):
        return url
    elif isinstance(url, tuple or list or set):
        try:
            if all(isinstance(url_i, str) for url_i in url):
                return [url_i for url_i in url]
            else:
                raise TypeError("此序列中存在非字符串类型的数据！")
        except TypeError as e:
            y_url = []
            n_url = []
            for url_i in url:
                if isinstance(url_i, str):
                    y_url.append(url_i)
                else:
                    n_url.append(url_i)
            print(e, "以下数据类型非字符串类型：", n_url, f"总计： {len(n_url)}个。")
            return y_url, n_url
    elif isinstance(url, dict):
        y_url_dict = {}
        n_url_dict = {}
        try:
            for key, value in url.items():
                if isinstance(value, str):
                    y_url_dict[key] = value
                else:
                    raise TypeError("此字典中存在非字符串类型数据！")
            return y_url_dict
        except TypeError as e:
            for key, value in url.items():
                if isinstance(value, str):
                    y_url_dict[key] = value
                else:
                    n_url_dict[key] = value
            print(e, "以下数据类型非字符串类型：", n_url_dict, f"总计： {len(n_url_dict)}个。")
            return y_url_dict, n_url_dict
    else:
        try:
            raise TypeError("请勿输入不被接收的数据类型！")
        except TypeError as e:
            print(e)
            return


class PreliminaryMatch(object):
    def __init__(self, url):
        self.url = inspection_url(url)
        self.au, self.pc, self.qu, self.fr = character_processing()

    def match(self):
        pattern = re.compile(r"(https?)://([{}]+)(/[{}]*)*(\?[{}]*)?(#[{}]*)?".format(self.au,
                                                                                      self.pc + "/",
                                                                                      self.qu,
                                                                                      self.fr), flags=re.ASCII)
        match_object = re.match(pattern, self.url)
        return match_object


class ParseMatch(object):
    def __init__(self, url, match_object):
        self.url = inspection_url(url)
        self.Mobject = match_object

    def parse_object(self):
        if self.Mobject:
            return get_part(self.url, self.Mobject)
        # else:
        #     return self.url

class TryToComplete(object):
    def __init__(self, args):
        self.args = args

    def try_to_complete(self):
        if isinstance(self.args, str):
            if "http://" or "https://" not in self.args:
                new_url = "https://" + self.args
                return {
                    self.args: new_url
                }
            elif
                pass
            else:
                return "！！！ -> 权威中包含非法字符,或者权威为空 <- !!!"


class ParseScheme(object):
    pass











url = "https:%2F/aaa"
# url = "https://www.baidu.com/"
obj = PreliminaryMatch(url=url).match()
# print(obj)
PM = ParseMatch(url, obj)
part = PM.parse_object()
print(part)
