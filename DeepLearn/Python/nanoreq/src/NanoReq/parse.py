from safe_chars import *
import re
import random
import idna
import os
import base64

def choice_with_assemble(safe_set: list, start_num: int, end_num: int) -> str:
    component = f"{''.join([random.choice(safe_set) for _ in range(random.randint(start_num, end_num))])}"
    return component


def create_part():
    scheme_list, userinfo_list, IP_list, host_list, port_list, path_list, query_list, fragment_list = [], [], [], [], [], [], [], []
    for _ in range(50):
        _scheme = f"{random.choice(alpha)}" + choice_with_assemble(safe_set=scheme, start_num=3, end_num=5)
        _userinfo = choice_with_assemble(safe_set=userinfo[:-1:], start_num=1, end_num=10) + ':' + choice_with_assemble(
            safe_set=userinfo[:-1:], start_num=8, end_num=16)
        _IPv4 = '.'.join([str(random.randint(0, 255)) for _ in range(4)])
        _IPv6_1 = '[' + ':'.join([str(f"{random.randint(0, 65535):04X}") for _ in range(8)]) + ']'
        _IPv6_2 = '[' + ':'.join(
            [str(f"{random.randint(0, 65535):04X}") for _ in range(random.randint(1, 3))]) + '::' + ':'.join(
            [str(f"{random.randint(0, 65535):04X}") for _ in range(random.randint(2, 3))]) + ']'
        _IPvNum = f'v{random.randint(7, 100)}.' + random.choice([_IPv6_1, _IPv6_2])
        _host_1 = '.'.join(
            [(''.join(random.choices(population=(alpha + digit), k=3)) + choice_with_assemble(safe_set=host[:-1:],
                                                                                              start_num=1,
                                                                                              end_num=3) +
              random.choice(alpha + digit)) for _ in range(random.randint(2, 5))]) + '.' + random.choice(
            common_tld + [''])
        _host_2 = '.'.join([random.choice(punycode) for _ in range(random.randint(2, 3))])
        _port = str(random.randint(0, 65535))
        _path = random.choice([''.join([('/' * random.randint(1, 4) + choice_with_assemble(safe_set=pchar, start_num=3,
                                                                                           end_num=7) + random.choice(
            ['/', ''])) for _ in range(random.randint(1, 5))]),
                               '', '/', '/index.html', '/login', '/gushiwen'
                               ])
        _query = '?' + '&'.join([
            f"{choice_with_assemble(safe_set=query, start_num=1, end_num=7)}={choice_with_assemble(safe_set=query, start_num=1, end_num=20)}"
            for _ in range(random.randint(1, 7))])

        _fragment = '#' + choice_with_assemble(safe_set=fragment, start_num=1, end_num=10)
        scheme_list.append(_scheme)
        userinfo_list.append(_userinfo)
        IP_list.append(_IPv4)
        IP_list.append(_IPv6_1)
        IP_list.append(_IPv6_2)
        IP_list.append(_IPvNum)
        host_list.append(_host_1)
        host_list.append(_host_2)
        port_list.append(_port)
        path_list.append(_path)
        query_list.append(_query)
        fragment_list.append(_fragment)
    return scheme_list, userinfo_list, IP_list, host_list, port_list, path_list, query_list, fragment_list


def choice(part):
    return random.choice(part)


def create_url(scheme_list, userinfo_list, IP_list, host_list, port_list, path_list, query_list, fragment_list):
    url_list = []
    for _ in range(500):
        scheme = choice(scheme_list)
        userinfo = choice(userinfo_list)
        IP = choice(IP_list)
        host = choice(host_list)
        port = choice(port_list)
        path = choice(path_list)
        query = choice(query_list)
        fragment = choice(fragment_list)
        '''
        选择性添加
        '''
        scheme_ = choice([scheme, *common_scheme])
        userinfo_ = choice([f"{userinfo}@", ''])
        host_ = choice([host, IP])
        port_ = choice([f":{port}", ''])
        path_ = path
        query_ = choice([query, ''])
        fragment_ = choice([fragment, ''])
        url = scheme_ + '://' + userinfo_ + host_ + port_ + path_ + query_ + fragment_
        url_list.append(url)
    return url_list


result = create_url(*create_part())


