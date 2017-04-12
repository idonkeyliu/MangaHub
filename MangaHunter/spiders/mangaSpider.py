# -*- coding:utf-8 -*-
import requests
import logging
from scrapy.spider import CrawlSpider
from scrapy.spider import Selector

class Spider(CrawlSpider):
    """docstring for ."""
    def __init__(self, arg):
        super(, self).__init__()
        self.arg = arg
