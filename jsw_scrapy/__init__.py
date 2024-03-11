# helper
from jsw_scrapy.helpers.alioss_store import AliOssStore

# pipeline
from jsw_scrapy.pipelines.base_pipeline import BasePipeline

# middleware
from jsw_scrapy.middlewares.request_proxy import RequestProxyMiddleware
from jsw_scrapy.middlewares.random_user_agent import RandomUserAgentMiddleware

import pkg_resources

version = pkg_resources.get_distribution('jsw-scrapy').version
__version__ = version

# next models/pipelines/spiders
