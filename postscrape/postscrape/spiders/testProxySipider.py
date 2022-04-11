from curses import meta
import scrapy


class ProxySpider(scrapy.Spider):
    name = 'proxy'
    # allowed_domains = ['thegreyhoundrecorder.com.au']
    # start_urls = ['https://quotes.toscrape.com/']
    custom_settings = {
        'HTTPPROXY_ENABLED': True
    }
    def start_requests(self):
        urls = [
            'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies',
            # 'https://quotes.toscrape.com/page/2/',
        ]

        for url in urls:
            yield scrapy.Request(url=url, 
            headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36"},
            meta={
                # 'dont_redirect':True,
                
            #     # 'handle_httpstatus_list':[301,302, 308],
                "proxy": "https://127.0.0.1:9999"
                },
                    callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = f'quotes-{page}.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log(f'Saved file {filename}')

        yield{"title": response.css('#firstHeading::text').get()}
    