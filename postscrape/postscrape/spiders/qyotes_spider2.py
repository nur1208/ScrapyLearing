import scrapy

from ..items import QuoteItem

class QuoteSpider2(scrapy.Spider):
    name="quote_2"
    start_urls=["https://quotes.toscrape.com/"]

    def parse(self, response):
        quotesWrapper = response.css("div.quote")
        item = QuoteItem()
        for quote in quotesWrapper:
            item["title"] = quote.css("span.text::text").get()
            item["author"] = quote.css("small.author::text").get()
            item["tag"] = quote.css("a.tag::text").extract()
            yield item

        next_page = response.css("li.next a::attr(href)").get()

        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)


        