# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import scrapy
from itemadapter import ItemAdapter
from urllib.parse import urlparse
from scrapy.pipelines.images import ImagesPipeline
from os.path import join,basename,dirname
# https://konachan.net/sample/7b58c0404bdb176e52fa2392082ae7a1/Konachan.com%20-%20329341%20sample.jpg
class AnimePicPipeline:
    def process_item(self, item, spider):
        return item
class myimages_pipeline(ImagesPipeline):
    # 这个方法是在发送下载请求之前调用的，其实这个方法本身就是去发送下载请求的
    # def get_media_requests(self, item, info):
    #     for url in item['image_urls']:
    #         yield scrapy.Request(url,meta={'name':item['info']})

    def file_path(self,request,response=None,info=None):
        path = urlparse(request.url).path
        return join(dirname(dirname(path)),basename(path))
    # def file_path(self, request, response=None, info=None, *, item=None):
    #     pass