# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo
class JobPipeline(object):
    def __init__(self):
        self.mfile=open(r"1.txt","ab")
        self.conn=pymongo.MongoClient()

    def __del__(self):
        self.mfile.close()
        self.conn.close()

    def process_item(self, item, spider):
        mstr=item["title"]+"=="+item["company"]+"=="+item["address_before"]+"=="+item["money"]+"=="+item["date"]+"\n"
        self.mfile.write(mstr.encode("utf-8"))
        self.conn.job.j1.insert({
            "title":item["title"],
            "company":item["company"],
            "address_before":item["address_before"],
            "money":item["money"],
            "date":item["date"],
        })
        # print(item["title"],item["company"],item["address_before"],item["money"],item["date"])


        return item
