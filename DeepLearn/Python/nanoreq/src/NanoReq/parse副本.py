import re
import urllib.parse
import urllib.request


a = 'ssssss/ss'
b = urllib.parse.urlsplit(a)
class Parse:
    def __init__(self, url):
        self.url = url

    @staticmethod
    def divide(url):
        rule = re.match(r"\b(?:.+?://|.{0}).+?(?:/*?|\?).*", url)
        if rule:
            return rule
        else:
            return None

    @staticmethod
    def split(rule):
        urlsplit = {}
        if rule is not None:
            url_ = rule.group()
            if '://' in url_:
                protocol, last_part = url_.split('//', 1)
                urlsplit['protocol'] = protocol
                if '/' in last_part:
                    first_part, last_part = re.split('/.+', last_part, 1)
                    urlsplit['first_part'] = first_part
                    urlsplit['last_part'] = last_part


