# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ErrorSpiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    userHref = scrapy.Field()
    title = scrapy.Field()
    userId = scrapy.Field()
    username = scrapy.Field()
    level = scrapy.Field()
    date = scrapy.Field()
    courseHref = scrapy.Field()
    coursename = scrapy.Field()
    answered = scrapy.Field()
    viewed = scrapy.Field()

