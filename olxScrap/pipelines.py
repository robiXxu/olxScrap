# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json

class OlxscrapPipeline(object):
  data = []
  def open_spider(self, spider):
    self.file = open('data.json', 'w')
  
  def close_spider(self, spider):
    line = json.dumps(self.data)
    self.file.write(line)
    self.file.close()

  def process_item(self, item, spider):
    self.data.append(dict(item))
    return item
