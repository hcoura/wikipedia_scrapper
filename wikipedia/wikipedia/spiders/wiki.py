# -*- coding: utf-8 -*-
import scrapy
from urllib.parse import urljoin
from wikipedia.items import Article, ArticleItemLoader

ARTICLE_LINK_XPATH = '//div[@id="bodyContent"]/descendant::a[re:test(@href,' \
    ' "^/wiki/[^:]*$")]/@href'
TITLE_XPATH = '//h1[@id="firstHeading"]/text()'
PARAGRAPH_XPATH = '//div[@class="mw-parser-output"]/p[1]/' \
    'descendant-or-self::*[self::a[not(starts-with(@href, "#cite"))] ' \
    'or self::b or self::p]/text()'
IMAGE_XPATH = '//div[@class="mw-parser-output"]/table/descendant::img/@src'


class WikiSpider(scrapy.Spider):
    name = 'wiki'
    allowed_domains = ['pt.wikipedia.org']
    start_urls = ["https://pt.wikipedia.org/wiki/Clube_Atl%C3%A9tico_Mineiro"]

    def parse(self, response):
        articles = response.xpath(ARTICLE_LINK_XPATH).extract()
        base_url = "https://pt.wikipedia.org/"
        articles = [urljoin(base_url, a) for a in articles]
        articles = list(set(articles))

        yield self.parse_article(response=response)

        for a in articles[:5]:
            yield scrapy.Request(a, callback=self.parse_article)

    def parse_article(self, response):
        a = ArticleItemLoader(item=Article(), response=response)
        a.add_value('url', response.url)
        a.add_xpath('title', TITLE_XPATH)
        a.add_xpath('paragraph', PARAGRAPH_XPATH)
        a.add_xpath('image_url', IMAGE_XPATH)
        return a.load_item()
