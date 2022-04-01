# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals

# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter
from scrapy.http import Response


class IgnoreRequest:
    """This middleware looks for requests with meta ignore_request=True,
    if found it will return an empty Response object.
    This is used for spider which doesn't crawl webpages but still
    net to be placed inside the scrapy project for convenience.
    """

    def process_request(self, request, **_):  # pylint: disable=no-self-use
        if not request.meta.get("ignore_request"):
            return None
        return Response(url=request.url)
