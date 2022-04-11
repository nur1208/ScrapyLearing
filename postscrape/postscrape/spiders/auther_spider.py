from curses import meta
import scrapy


class AuthorSpider(scrapy.Spider):
    name = 'author'

    # start_urls = ['https://quotes.toscrape.com/']

    def start_requests(self):
        urls = [
            'https://quotes.toscrape.com/page/1/',
            # 'https://quotes.toscrape.com/page/2/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, meta={'dont_redirect':True,
                'handle_httpstatus_list':[301,302, 308],
                "proxy": "https://127.0.0.1:9999"},
                    callback=self.parse)

    def parse(self, response):
        author_page_links = response.css('.author + a')
        yield from response.follow_all(author_page_links, self.parse_author)

        pagination_links = response.css('li.next a')
        yield from response.follow_all(pagination_links, self.parse)

    def parse_author(self, response):
        def extract_with_css(query):
            return response.css(query).get(default='').strip()

        yield {
            'name': extract_with_css('h3.author-title::text'),
            'birthdate': extract_with_css('.author-born-date::text'),
            'bio': extract_with_css('.author-description::text'),
        }