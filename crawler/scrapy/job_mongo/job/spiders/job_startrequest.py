# -*- coding: utf-8 -*-
import scrapy
import lxml
import lxml.etree
from job import items


class Job2Spider(scrapy.Spider):
    name = 'job1101_2'
    allowed_domains = ['51job.com']
    # start_urls = ['http://search.51job.com/list/040000,000000,0000,00,9,99,python,2,1.html']
    def start_requests(self):
        headers={"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36"}
        for i in range(1,73):
            url="http://search.51job.com/list/040000,000000,0000,00,9,99,python,2,"+str(i)+".html"
            request=scrapy.Request(url,headers=headers)
            yield request




    def parse(self, response):
        count=0
        items_list=items.JobItem()
        for i in range(4,54):

            if len(response.xpath("//*[@id=\"resultList\"]/div["+str(i)+"]/p/span/a/text()").extract())==0:
                title = "#"
            else:
                title=response.xpath("//*[@id=\"resultList\"]/div["+str(i)+"]/p/span/a/text()").extract()[0].strip()
            if len(response.xpath("//*[@id=\"resultList\"]/div["+str(i)+"]/span[1]/a/text()").extract())==0:
                company = "#"
            else:
                company=response.xpath("//*[@id=\"resultList\"]/div["+str(i)+"]/span[1]/a/text()").extract()[0]
            if len(response.xpath("//*[@id=\"resultList\"]/div["+str(i)+"]/span[2]/text()").extract())==0:
                address = "#"
            else:
                address=response.xpath("//*[@id=\"resultList\"]/div["+str(i)+"]/span[2]/text()").extract()[0]
            if len(response.xpath("//*[@id=\"resultList\"]/div["+str(i)+"]/span[3]/text()").extract())==0:
                money = "#"
            else:
                money=response.xpath("//*[@id=\"resultList\"]/div["+str(i)+"]/span[3]/text()").extract()[0]
            if len(response.xpath("//*[@id=\"resultList\"]/div["+str(i)+"]/span[4]/text()").extract())==0:
                date = "#"
            else:
                date=response.xpath("//*[@id=\"resultList\"]/div["+str(i)+"]/span[4]/text()").extract()[0]
            items_list["title"]=title
            items_list["company"]=company
            items_list["address_before"]=address
            items_list["money"]=money
            items_list["date"]=date
            yield items_list
            # print(title)
            # print(company)
            # print(address_before)
            # print(money)
            # print(date)




        pass
















pass
