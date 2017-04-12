# -*- coding:utf-8 -*-

import requests
import logging
from scrapy.spider import BaseSpider
from scrapy.spider import Selector
from MangaHunter.items import MangaItem

class Spider(BaseSpider):
    name = "mangaHunterSpider"

    #设置开始抓取的网址
    start_urls = ["http://www.ac.qq.com/"]

    def parse(self, response):
        filename = response.url.split("/")[-2]
        open(filename, 'wb').write(response.body)

    def parse_ph_info(self,response):
        mangaItem = MangaItem()
        selector = Selector(response)
        _ph_info = re.findall('flashvars_.*?=(.*?);\n',selector.extract())
        _ph_info_json = json.loads(_ph_info[0])

        #获取标题与封面地址
        title = _ph_info_json.get('title')
        mangaItem['title'] = title
        cover_url = _ph_info_json.get('cover_url')
        mangaItem['cover_url'] = cover_url

        yield mangaItem
