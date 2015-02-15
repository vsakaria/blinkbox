import scrapy

from blinkbox.items import BlinkboxItem

class DmozSpider(scrapy.Spider):
    name = "blinkbox_lastest"
    allowed_domains = ["blinkbox.com"]
    start_urls = [
        "http://www.blinkbox.com/movies"
    ]

    def parse(self, response):
      item = BlinkboxItem()
      for sel in response.css('.jsPaginationContainer ol li article h2 a'):
            item['title'] = sel.xpath('/text()').extract()
            item['href'] = sel.xpath('@href').extract()
            yield item

      # title = response.css('.jsPaginationContainer ol li article h2')
      # href = response.css('.jsPaginationContainer ol li article h2 a')
