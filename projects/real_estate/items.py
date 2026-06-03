# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from itemloaders.processors import MapCompose, Join


def description_in(description):
    return description.strip()


def description_out(description):
    labels = description[0:3]
    values = description[3:]
    output = {
        labels[0]: "".join(values[0]),
        labels[1]: "".join(values[1:-1]),
        labels[2]: "".join(values[-1]),
    }
    return output


class RealEstateItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field(output_processor=Join())
    description = scrapy.Field(input_processor=MapCompose(description_in), output_processor=description_out)
    price = scrapy.Field(output_processor=Join())
    agency = scrapy.Field(output_processor=Join())
