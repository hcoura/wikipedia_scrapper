# -*- coding: utf-8 -*-
import scrapy
from scrapy.loader.processors import TakeFirst, MapCompose, Join
from scrapy.loader import ItemLoader


class Article(scrapy.Item):
    url = scrapy.Field()
    title = scrapy.Field()
    paragraph = scrapy.Field()
    image_url = scrapy.Field()
    image = scrapy.Field()


class ArticleItemLoader(ItemLoader):
    def format_image(image_url):
        return "http:" + image_url

    default_input_processor = TakeFirst()
    default_output_processor = TakeFirst()

    image_url_in = MapCompose(format_image)
    paragraph_in = Join('')
