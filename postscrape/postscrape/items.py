# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class PostscrapeItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class QuoteItem(scrapy.Item):
    title = scrapy.Field()
    author = scrapy.Field()
    tag = scrapy.Field()
