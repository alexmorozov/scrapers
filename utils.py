#--coding: utf8--

from StringIO import StringIO

from lxml import html
import requests


class Page(object):
    def __init__(self, url):
        self.tree = html.fromstring(requests.get(url).content)

    def css(self, selector):
        return self.tree.cssselect(selector)
