# -*- coding: utf-8 -*-
import scrapy

'''
class BooksSpider(scrapy.Spider):
    name = "books"
    allowed_domains = ["books.toscrape.com"]
    start_urls = [
        'http://books.toscrape.com/',
    ]

    def parse(self, response):
        for book_url in response.css("article.product_pod > h3 > a ::attr(href)").extract():
            yield scrapy.Request(response.urljoin(book_url), callback=self.parse_book_page)
        next_page = response.css("li.next > a ::attr(href)").extract_first()
        if next_page:
            yield scrapy.Request(response.urljoin(next_page), callback=self.parse)

    def parse_book_page(self, response):
        item = {}
        product = response.css("div.product_main")
        item["title"] = product.css("h1 ::text").extract_first()
        item['category'] = response.xpath(
            "//ul[@class='breadcrumb']/li[@class='active']/preceding-sibling::li[1]/a/text()"
        ).extract_first()
        item['description'] = response.xpath(
            "//div[@id='product_description']/following-sibling::p/text()"
        ).extract_first()
        item['price'] = response.css('p.price_color ::text').extract_first()
        yield item
        '''

# https://link.coupang.com/re/AFFSDP?lptag=AF1234567&pageKey=2128457892&itemId=3612631996&vendorItemId=71598275778&traceid=V0-153-cdf3ae22673fa330
class QuotesSpider(scrapy.Spider):
    name = "coupang"
    start_urls = [
        'https://link.coupang.com/re/AFFSDP?lptag=AF1234567&pageKey=2128457892&itemId=3612631996&vendorItemId=71598275778&traceid=V0-153-cdf3ae22673fa330',
    ]

    def parse(self, response):
        item = {}
        item['title'] = response.css('#contents > div.prod-atf > div > div.prod-buy.new-oos-style.not-loyalty-member.eligible-address.without-subscribe-buy-type.DISPLAY_0 > div.prod-buy-header > h2').extract_first()
        yield item        

