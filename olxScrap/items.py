# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import Join, MapCompose, TakeFirst

import utils

class Ad(scrapy.Item):
  url = scrapy.Field()
  title = scrapy.Field(
    input_processor=MapCompose(utils.clean),
    output_processor=Join()
  )
  location = scrapy.Field(
    input_processor=MapCompose(utils.clean),
    output_processor=TakeFirst()
  )
  description = scrapy.Field(
    input_processor=MapCompose(utils.clean),
    output_processor=TakeFirst()
  )
  price = scrapy.Field(
    input_processor=MapCompose(utils.clean),
    output_processor=Join()
  )
  addedAt = scrapy.Field(
    input_processor=MapCompose(utils.clean,utils.cleanDate),
    output_processor=Join()
  )

  images = scrapy.Field()
  otherProperties = scrapy.Field()