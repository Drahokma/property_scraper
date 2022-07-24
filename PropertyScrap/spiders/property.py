import scrapy
from scrapy import Selector
from scrapy.http import Request
from selenium import webdriver
from time import sleep
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from scrapy.crawler import CrawlerProcess
from PropertyScrap.items import PropertyscrapItem
#from ..items import PropertyscrapItem
import json
    
class PropertySpider(scrapy.Spider):
    name = 'property'
    allowed_domains = ['sreality.cz']  
    def start_requests(self):
        crawl = True
        page = 1
        self.property_count = 0          
        #while self.property_count < 60:
        for page in range(1,2):
            self.url = 'https://www.sreality.cz/hledani/prodej/byty?strana='+str(page)
            options = webdriver.ChromeOptions()
            options.headless = True            
            self.driver = webdriver.Chrome(ChromeDriverManager().install(),options=options)
            self.driver.get(self.url)          
            yield Request(self.url, callback=self.parse) 
            #page = page + 1 

            

    def parse(self, response):         
        properties = response.xpath("//div[@class='property ng-scope']")
   
        # scrape property in properties list
        for property in properties:
            # xpath of property name 
            property_URL = property.css('a').attrib['href']  
            property_name = property.css('span.name.ng-binding::text').get()
            property_locality = property.css('span.locality.ng-binding::text').get()
            self.property_count = self.property_count + 1
            if self.property_count <= 60:
            # init item
                property_item = PropertyscrapItem()
                property_item['url'] = property_URL
                property_item['name'] = property_name
                property_item['locality'] = property_locality
                yield{ "url" : property_URL,
                       "name" : property_name,
                       "locality":property_locality
                }                 
                return property_item

        
                                       
        self.driver.close()

# main driver
if __name__ == '__main__':
    # run scraper
    process = CrawlerProcess()
    process.crawl(PropertySpider)
    process.start()           

        