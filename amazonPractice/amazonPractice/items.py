# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AmazonpracticeItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    prodcut_name = scrapy.Field()
    prodcut_author = scrapy.Field()
    prodcut_price = scrapy.Field()
    prodcut_imageUrl = scrapy.Field()


    