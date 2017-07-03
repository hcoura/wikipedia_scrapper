# -*- coding: utf-8 -*-
from urllib.request import urlretrieve
from os import path, makedirs


class WikipediaPipeline(object):
    def __init__(self):
        self.image_dir = path.dirname(path.abspath(__file__)) + "/../images"
        if not path.exists(self.image_dir):
            makedirs(self.image_dir)

    def process_item(self, item, spider):
        try:
            image_url = item["image_url"]
            filename = image_url.split("/")[-1]
            filepath = self.image_dir + "/" + filename
            urlretrieve(image_url, filepath)
            item["image"] = filename
            return item
        except Exception as e:
            return item
