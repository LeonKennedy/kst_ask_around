# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from taobao_ask_around.items import TaobaoAskAroundItem
from pymongo import MongoClient
import json, logging

class TaobaoAskAroundPipeline(object):

    def __init__(self):
        client = MongoClient('localhost', 27017)
        db = client.taobao
        self.collection = db.ask_around
        self.datafile = 'ask_data-2.json'

    def process_item(self, item, spider):
        a = self.collection.find_one({'goods_id':item['goods_id']})
        if not a:
            logging.info("[pipline] insert item")
            self.collection.insert(dict(item))
        '''
        jsonstr = json.dumps(dict(item), ensure_ascii=False) + '\n'
        with open(self.datafile, 'a+') as f:
            f.write(jsonstr)
        '''
        #return item


