from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor
from example import items
from scrapy_redis.spiders import RedisCrawlSpider


class MyCrawler(RedisCrawlSpider):
    count = 0
    """Spider that reads urls from redis queue (myspider:start_urls)."""
    name = 'mycrawler_redis'
    redis_key = 'mycrawler:start_urls'

    rules = (
        # follow all links
        Rule(LinkExtractor(allow=r"http://sz.ganji.com/shouji/o\d+/")),
        Rule(LinkExtractor(allow=r"http://zhuanzhuan.ganji.com/detail/\d+z.shtml"), callback="parse_content_one"),
        Rule(LinkExtractor(allow=r"http://sz.ganji.com/shouji/\d+x.htm"), callback="parse_content_two"),
    )

    # def __init__(self, *args, **kwargs):
    #     # Dynamically define the allowed domains list.
    #     domain = kwargs.pop('domain', '')
    #     self.allowed_domains = filter(None, domain.split(','))
    #     super(MyCrawler, self).__init__(*args, **kwargs)

    def parse_content_one(self, response):
        items_list=items.GanjiItem()
        self.count+=1
        print("+++++++++++++",response)
        title=response.css(".info_titile::text")
        money=response.css(".price_now > i::text")
        content=response.css(".baby_kuang > p::text")
        print(title.extract()[0])
        print(money.extract()[0])
        content = "#".join(content.extract())
        print(content)
        items_list["title"]=title.extract()[0]
        items_list["money"]=money.extract()[0]
        items_list["content"]=content
        yield items_list
        print("--------------------",self.count)
        pass
    def parse_content_two(self, response):
        items_list = items.GanjiItem()
        self.count+=1
        print("===========",response)
        title=response.css(".col-cont h1::text")
        money=response.css(".det-infor > li > i::text")
        content=response.css(".second-sum-cont span::text")
        print(title.extract()[0])
        print(money.extract()[0])
        content="#".join(content.extract())
        print(content)
        items_list["title"] = title.extract()[0]
        items_list["money"] = money.extract()[0]
        items_list["content"] = content
        yield items_list
        print("--------------------",self.count)

