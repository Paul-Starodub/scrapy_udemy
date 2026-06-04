import scrapy
from scrapy import FormRequest, Request


class LoginSpider(scrapy.Spider):
    name = "login"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["https://quotes.toscrape.com"]

    def parse_login(self, response):
        ret = FormRequest.from_response(
            response,
            formdata={"username": "amorallex", "password": "vovk7777"},
        )
        self.logger.info("Sent: %s", ret.body)
        return ret

    async def start(self):
        yield Request(url="https://quotes.toscrape.com/login", callback=self.parse_login)

    def parse(self, response, **kwargs):
        pass
