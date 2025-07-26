def Proxy(**kwargs):
    Charles = kwargs['Charles']
    if Charles:
        return tuple(['127.0.0.1', 8888])
    else:
        protocol = kwargs['protocol']
        IP = kwargs['IP']
        port = kwargs['port']
        proxies = f"{protocol}://{IP}:{port}"
        return proxies


