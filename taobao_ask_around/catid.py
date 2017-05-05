#!/usr/bin/env python
#-*- coding: utf-8 -*-
# @Filename: catid.py
# @Author: olenji - lionhe0119@hotmail.com
# @Description: ---
# @Create: 2017-05-02 19:20:04
# @Last Modified: 2017-05-02 19:20:04
#
import pymysql

class Catid:

    def __init__(self):
        self.connect = pymysql.connect(host='119.23.72.240',user = 'kst',password='kst410', db='kst', charset='utf8mb4')
        self.cur_query = self.connect.cursor()
        self.cur_update = self.connect.cursor()
        self.table = 'taobao_category'


    def getcatid(self):
        #sql = "select * from %s where cat is not null and stat <> 'scrapy' and stat <> 'scrapying' limit 1" % self.table
        sql = "select * from %s where stat = 'finish' limit 10" % self.table
        self.cur_query.execute(sql)
        res = list()
        for record  in self.cur_query.fetchall():
            res.append(record[3])
            usql = "update %s set stat = 'scrapying' where id = %d" %( self.table, record[0])
            self.cur_update.execute(usql)
        self.cur_update.close()
        self.connect.commit()
        return res

    def __del__(self):
        self.cur_query.close()
        self.connect.close()


c = Catid()
cat_id_list = c.getcatid()
#print(cat_id_list)


