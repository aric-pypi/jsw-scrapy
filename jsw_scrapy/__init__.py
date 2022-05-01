import pkg_resources

version = pkg_resources.get_distribution('jsw-scrapy').version
__version__ = version

# next base
from jsw_scrapy.base.every import every
