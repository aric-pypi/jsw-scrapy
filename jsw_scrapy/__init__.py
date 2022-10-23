# spider
from jsw_scrapy.spiders.base_spider import BaseSpider
from jsw_scrapy.spiders.base_peewee_spider import BasePeeweeSpider

# pipeline
from jsw_scrapy.pipelines.base_pipeline import BasePipeline

# model
from jsw_scrapy.models.base_peewee_model import BasePeeweeModel
from jsw_scrapy.models.base_model import BaseModel
import pkg_resources

version = pkg_resources.get_distribution('jsw-scrapy').version
__version__ = version

# next models/pipelines/spiders
