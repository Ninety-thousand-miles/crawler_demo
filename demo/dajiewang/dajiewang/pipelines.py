# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import MySQLdb


class DajiewangPipeline(object):
    def __init__(self):
        self.conn = MySQLdb.connect(host='localhost', user='root', password='haopeng', port=3306, db='crawler',
                                    charset='utf8')
        self.cursor = self.conn.cursor()
        self.sql = 'insert into dajiewang values(%s,%s,%s,%s,%s,%s,%s)'
        self.count = 0

    def process_item(self, item, spider):
        # 入库
        try:
            self.count += 1
            self.cursor.execute(self.sql,
                                (item['url'], item['job_name'], item['salary'], item['require'],
                                 item['company'], item['msg'], item['describe']))
            if self.count == 100:
                self.count = 0
            self.conn.commit()
        except:
            pass

    def close_spider(self, spider):
        self.cursor.close()
        self.conn.close()
