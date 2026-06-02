import scrapy


class ListingsSpider(scrapy.Spider):
    name = "listings"
    allowed_domains = ["arizonarealestate.com"]
    start_urls = ["https://arizonarealestate.com"]

    def parse(self, response):
        pass
