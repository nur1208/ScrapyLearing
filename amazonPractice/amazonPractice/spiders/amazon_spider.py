import scrapy
from ..items import AmazonpracticeItem

class AmazonSpider(scrapy.Spider):
    name="amazon"
    # start_urls = [
    #     "https://www.amazon.com/s?bbn=283155&rh=n%3A283155%2Cp_n_publication_date%3A1250226011&dc&qid=1649625434&rnid=1250225011&ref=lp_1000_nr_p_n_publication_date_0"
    # ]

    page_num = 2    

    def start_requests(self):
        urls = [
            'https://www.amazon.com/s?bbn=283155&rh=n%3A283155%2Cp_n_publication_date%3A1250226011&dc&qid=1649625434&rnid=1250225011&ref=lp_1000_nr_p_n_publication_date_0',
        ]

        for url in urls:
            yield scrapy.Request(url=url, 
            meta={
                "proxy": "https://127.0.0.1:9999"
                },
                    callback=self.parse)

    def parse(self, response):
        items = AmazonpracticeItem()
        booksWrapper = response.css(".s-card-border")

        for book in booksWrapper:

            prodcut_name = book.css(".a-size-medium::text").get()
            prodcut_author = book.css(".a-color-secondary .a-size-base.s-link-style").css("::text").get()
            prodcut_price = book.css(".a-price-fraction , .a-price-whole").css("::text").get()
            prodcut_imageUrl = book.css(".s-image::attr(src)").get()
            

            items["prodcut_name"] = prodcut_name
            items["prodcut_author"] = prodcut_author
            items["prodcut_price"] = prodcut_price
            items["prodcut_imageUrl"] = prodcut_imageUrl

            yield items
        next_page = f"https://www.amazon.com/s?i=stripbooks&bbn=283155&rh=n%3A283155%2Cp_n_publication_date%3A1250226011&dc&page={AmazonSpider.page_num}&qid=1649627559&rnid=1250225011&ref=sr_pg_2"

        if AmazonSpider.page_num <= 100:
            AmazonSpider.page_num += 1
            yield response.follow(next_page, callback=self.parse)

    