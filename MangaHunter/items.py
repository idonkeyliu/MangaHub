# -*- coding:utf-8 -*-

from scrapy import Item, Field

class MangaItem(Item):
    title = Field()
    cover = Field()
