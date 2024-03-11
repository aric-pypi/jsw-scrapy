import requests

"""
@Usage:
1. Add the following to your settings.py file:
DOWNLOADER_MIDDLEWARES = {
    'jsw_scrapy.middlewares.request_proxy.RequestProxyMiddleware': 543,
}

2. Add the following to your settings.py file if you want to use a custom list of user agents:
REQUEST_PROXY_LOCAL = False  # optional, default is False
REQUEST_PROXY_URL = 'http://localhost:5010/get/'  # optional, default is 'http://localhost:5010/get/'
"""

class RequestProxyMiddleware(object):
    def __init__(self, **kwargs):
        self.settings = kwargs

    @classmethod
    def from_crawler(cls, crawler):
        return cls(**crawler.settings)

    def process_request(self, request, spider):
        is_dynamic = self.settings.get('REQUEST_PROXY_LOCAL', False)
        static_proxy_url = 'http://127.0.0.1:9090'
        proxy_url = self.get_proxy_url(spider) if is_dynamic else static_proxy_url
        spider.logger.info(f'💀 Using proxy: {proxy_url}')
        request.meta['proxy'] = proxy_url
        return None

    @classmethod
    def get_proxy_url(cls):
        proxy_url = cls.settings.get('REQUEST_PROXY_URL', 'http://localhost:5010/get/')
        res = requests.get(proxy_url)
        json_data = res.json()
        proxy = json_data.get('proxy')
        is_https = json_data.get('https')
        protocol = 'https' if is_https else 'http'
        return f'{protocol}://{proxy}'
