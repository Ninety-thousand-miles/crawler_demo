# -*- coding: utf-8 -*-
import scrapy
import re
from ..items import DajiewangItem


class DjwSpiderSpider(scrapy.Spider):
    name = 'djw_spider'
    # allowed_domains = ['job.dajie.com/qz2']
    start_urls = ['http://job.dajie.com/']

    def start_requests(self):
        for i in range(1, 11504):
            url = 'https://job.dajie.com/qz2-p%s/' % i
            yield scrapy.Request(url=url, dont_filter=True, callback=self.get_list)

    def get_list(self, response):
        data_urls = response.xpath('//div[@class="jobList"]/ul/li/@data-url').getall()
        for detailurl in data_urls:
            yield scrapy.Request(url=detailurl,dont_filter=True,callback=self.get_detail)

    def get_detail(self,response):
        url = response.url
        job_name = response.xpath('//div[@class="job-msg-top-text"]/span/@title').get()
        salary = response.xpath('//span[@class="job-money"]/em/text()').get()
        require = '/'.join(response.xpath('//div[@class="job-msg-center"]/ul/li/span//text()').getall())
        company = ''.join(response.xpath('//div[@class="i-corp-base-info"]/p/a/text()').get()).strip()
        msg = '/'.join(response.xpath('//div[@class="job-msg-bottom"]/ul/li//text()').getall())
        describe = ''.join(response.xpath('//div[@class="position-data "]/pre/text()').get()).replace('\n', '')
        # print(url,job_name, salary, require, company, msg, describe)
        item = DajiewangItem(
            url = url,
            job_name = job_name,
            salary= salary,
            require = require,
            company = company,
            msg = msg,
            describe = describe,
        )
        yield item