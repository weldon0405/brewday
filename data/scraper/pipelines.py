# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
import os

from scraper.items import CerealsItem
from scraper.items import HopsItem
from scraper.items import YeastItem

CEREALS_DIR = './cereals'
HOPS_DIR = './hops'
YEAST_DIR = './yeast'


class CerealsPipeline(object):

    def process_item(self, item, spider):
        if not isinstance(item, CerealsItem):
            return item
        filename = item['name'].lower().replace(" ", "_")
        filename = filename.replace(",", "")
        filename = filename.replace("(", "")
        filename = filename.replace(")", "")
        filename = filename.replace("/", "_")
        filename = filename.replace("-", "_")
        filename = filename.replace("___", "_")
        filename = filename.replace("__", "_")
        filename = filename.replace("_-", "_")
        filename = "{}.json".format(filename)
        filepath = os.path.join(os.path.abspath(CEREALS_DIR), filename)
        with open(filepath, 'wb') as f:
            line = json.dumps(dict(item))
            f.write(line)
        return item


class HopsPipeline(object):

    def process_item(self, item, spider):
        if not isinstance(item, HopsItem):
            return item
        filename = item['name'].lower().replace(" ", "_")
        filename = filename.replace("(", "")
        filename = filename.replace(")", "")
        filename = filename.replace("'", "")
        filename = filename.replace("-", "_")
        filename = "{}.json".format(filename)
        filepath = os.path.join(os.path.abspath(HOPS_DIR), filename)
        with open(filepath, 'wb') as f:
            line = json.dumps(dict(item))
            f.write(line)
        return item


class YeastPipeline(object):

    def process_item(self, item, spider):
        if not isinstance(item, YeastItem):
            return item
        item[u'name'] = item[u'name'].replace('\u2013', '-')

        if item['yeast_id']:
            identifier = item['yeast_id'].lower()
        else:
            identifier = item['name'].lower()
        filename = '{}_{}'.format(item['manufacturer'].lower(),
                                  identifier)
        filename = filename.replace(" ", "_")
        filename = filename.replace("-", "_")
        filename = filename.replace("/", "_")
        filename = "{}.json".format(filename)
        filepath = os.path.join(os.path.abspath(YEAST_DIR), filename)
        with open(filepath, 'wb') as f:
            line = json.dumps(dict(item))
            f.write(line)
        return item
