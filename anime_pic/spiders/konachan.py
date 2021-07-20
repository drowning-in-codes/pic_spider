import time

import scrapy
from scrapy.linkextractors import LinkExtractor
from ..items import AnimePicItem


class KonachanSpider(scrapy.Spider):
    name = 'konachan'
    allowed_domains = ['konachan.net']
    start_urls = ['https://konachan.net/post']

    # 爬取一定页数
    # for i in range(1, 51):
    #     url = "https://konachan.net/post?page={}".format(i)
    #     start_urls.append(url)
    def parse(self, response):
        # 爬取每个图片的地址
        # 并交给pic_parse处理
        le = LinkExtractor(restrict_xpaths="//div[@class='inner']")
        for link in le.extract_links(response):
            yield scrapy.Request(link.url, callback=self.pic_parse)

        # 爬取下一页链接
        # 交给parse继续处理
        # le = LinkExtractor(restrict_xpaths="//div[@class='pagination']")
        # links = le.extract_links(response)
        # if links:
        #     next_url = links[-1].url
        #     yield scrapy.Request(next_url, callback=self.parse)
        href = response.xpath("//div[@class='pagination']/a[@class='next_page']/@href").extract_first()
        if href:
            next_url = response.urljoin(href)
            yield scrapy.Request(next_url,callback=self.parse)
    def pic_parse(self, response):
        href = response.xpath("//div[@id='right-col']//@src").extract() #这必须是列表
        info = response.xpath("//div[@id='right-col']//@alt").extract_first()
        # url = response.urljoin(href)
        pic_item = AnimePicItem()
        pic_item['image_urls'] = href
        info = info.split(" ")[0:2]
        pic_item['info'] = "_".join(info)
        return pic_item
