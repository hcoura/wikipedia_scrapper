# -*- coding: utf-8 -*-
BOT_NAME = 'wikipedia'

SPIDER_MODULES = ['wikipedia.spiders']
NEWSPIDER_MODULE = 'wikipedia.spiders'
ROBOTSTXT_OBEY = True

ITEM_PIPELINES = {
   'wikipedia.pipelines.WikipediaPipeline': 300,
}
