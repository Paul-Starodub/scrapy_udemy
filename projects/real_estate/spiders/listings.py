import scrapy

from real_estate.items import RealEstateItem
from scrapy.loader import ItemLoader


class ListingsSpider(scrapy.Spider):
    name = "listings"
    allowed_domains = ["arizonarealestate.com"]
    start_urls = [
        "https://www.arizonarealestate.com/maricopa/",
        "https://www.arizonarealestate.com/goodyear/",
        "https://www.arizonarealestate.com/tempe/",
    ]

    def parse(self, response):
        gallery = response.xpath('//div[@class="si-listings-column"]')
        for listing in gallery:
            item = ItemLoader(item=RealEstateItem(), response=response, selector=listing)
            item.add_xpath("name", ".//div[@class='si-listing__title-main']/text()")
            item.add_xpath(
                "name", ".//div[@class='si-listing__neighborhood']/span[@class='si-listing__neighborhood-place']/text()"
            )
            item.add_xpath(
                "description", './/div[@class="si-listing__info"]//div[@class="si-listing__info-label"]/text()'
            )
            item.add_xpath(
                "description",
                './/div[@class="si-listing__info"]//div[@class="si-listing__info-value"]/descendant::*/text()',
            )
            item.add_xpath("price", './/div[@class="si-listing__photo-price"]/span/text()')
            item.add_xpath("agency", './/div[@class="si-listing__footer"]/div/text()')
            yield item.load_item()

            # item = RealEstateItem()
            # item["name"] = listing.xpath(
            #     './/div[@class="si-listing__title-main"]/text() | .//div[@class="si-listing__neighborhood"]/span[@class="si-listing__neighborhood-place"]/text()'
            # ).getall()
            # item["description"] = listing.xpath(
            #     './/div[@class="si-listing__info"]//div[@class="si-listing__info-label"]/text() | .//div[@class="si-listing__info"]//div[@class="si-listing__info-value"]/descendant::*/text()'
            # ).getall()
            # item["description"] = ["".join(x.split()) for x in item["description"]]
            # item["price"] = listing.xpath('.//div[@class="si-listing__photo-price"]/span/text()').get()
            # item["agency"] = listing.xpath('.//div[@class="si-listing__footer"]/div/text()').get()
            # yield item
