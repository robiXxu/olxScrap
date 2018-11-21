# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import Join, MapCompose, TakeFirst
from w3lib.html import remove_tags


def clean(value):
  return value.strip()

class Ad(scrapy.Item):
  title = scrapy.Field(
    input_processor=MapCompose(remove_tags,clean),
    output_processor=Join()
  )
  location = scrapy.Field(
    input_processor=MapCompose(remove_tags,clean),
    output_processor=TakeFirst()
  )
  description = scrapy.Field(
    input_processor=MapCompose(remove_tags,clean),
    output_processor=TakeFirst()
  )
  price = scrapy.Field(
    input_processor=MapCompose(remove_tags,clean),
    output_processor=Join()
  )
  images = scrapy.Field()
