import scrapy

class QiandaoItem(scrapy.Item):
    title = scrapy.Field()
    link = scrapy.Field()
    date = scrapy.Field()
