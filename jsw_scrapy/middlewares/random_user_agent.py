import random

"""
@Usage:
    1. Add the following to your settings.py file:
    DOWNLOADER_MIDDLEWARES = {
        'jsw_scrapy.middlewares.random_user_agent.RandomUserAgentMiddleware': 543,
    }
    
    2. Add the following to your settings.py file if you want to use a custom list of user agents:
    USER_AGENT_LIST = []        # optional
    USER_AGENT_VERBOSE = True   # optional, default is False
"""

USER_AGENT_LIST = [
    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2226.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.4; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2225.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2225.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2224.3 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.93 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2049.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 4.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2049.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.67 Safari/537.36",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.67 Safari/537.36",
    "Mozilla/5.0 (X11; Open BSD i386) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36",
]


class RandomUserAgentMiddleware:
    def __init__(self, **kwargs):
        self.settings = kwargs

    @classmethod
    def from_crawler(cls, crawler):
        return cls(**crawler.settings)

    def process_request(self, request, spider):
        user_agent_list = self.settings.get("USER_AGENT_LIST", USER_AGENT_LIST)
        user_agent = random.choice(user_agent_list)
        request.headers['User-Agent'] = user_agent
        if self.settings.get("USER_AGENT_VERBOSE"):
            spider.logger.info(f'😎 Request: {request.url} using User-Agent: {user_agent}')
