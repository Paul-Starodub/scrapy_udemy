# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from itemloaders.processors import MapCompose


def description_in(description):
    return description.strip()


class RealEstateItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    description = scrapy.Field(input_processor=MapCompose(description_in))
    price = scrapy.Field()
    agency = scrapy.Field()
