# importing the scrapy module
import scrapy
from ..items import SimpleCrawlerItem


class FashionSpider(scrapy.Spider):
    #name of spider
    name = 'fashion'
    #list of allowed domains
    allowed_domains = ['matchesfashion.com']
    #starting url
    start_urls = ['https://www.matchesfashion.com/intl/mens/shop/shoes']
    base_url = 'https://www.matchesfashion.com'

    # change total_page count to the number of pages you want to scrap
    total_page = 7
    start_page = 0

    def parse(self, response):
        items = SimpleCrawlerItem()
        all_items = response.css('.lister__item')
        #Extracting the  product information using css selectors
        #for listing all the items in the website
        for product in all_items:
            product_name = product.css('.lister__item__title::text').extract()
            product_price = product.css('.lister__item__price-full::text').extract()
            product_image_link = "https://www.matchesfashion.com/" + str(product.css('.lazy::attr(data-original)').extract())[2:]
            product_url = "https://www.matchesfashion.com" + str(product.css('.lister__item__inner a::attr(href)').extract()[0])
            product_brand = product.css('.lister__item__details::text').extract()

            items['product_name'] = product_name
            items['product_price'] = product_price
            items['product_image_link'] = product_image_link
            items['product_url'] = product_url
            items['product_brand'] = product_brand
            yield items
            #return or give the scraped info of all the items to scrapy
            #for pagination , so that we can extract data from the next page
            #base_url is used in order to get the content of previous page along with the next page as well
        print('next page url')
        next_page_partial_url = response.css('.redefine__right__pager .next a::attr(href)').extract()[:0]
        print('NEXT URL = ', next_page_partial_url)
        next_page_url = self.base_url + next_page_partial_url
        print('NEXT URL = ', next_page_url)
        
        
        #for moving to next page addition of 1 is there 
        self.start_page += 1
        if self.start_page < self.total_page:
            yield scrapy.Request(next_page_url, callback=self.parse)
