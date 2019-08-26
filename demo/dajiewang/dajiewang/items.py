# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DajiewangItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    url = scrapy.Field()
    job_name = scrapy.Field()
    salary = scrapy.Field()
    require = scrapy.Field()
    company = scrapy.Field()
    msg = scrapy.Field()
    describe = scrapy.Field()
