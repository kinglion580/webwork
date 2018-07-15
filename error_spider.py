import scrapy

class CourseErrorSpider(scrapy.Spider):
    name='course-error'

    def start_requests(self):
        url_tmpl='https://www.shiyanlou.com/questions/?type=course_error&page={}'
        urls=(url_tmpl.format(i) for i in range(1,16))
        for url in urls:
            yield scrapy.Request(url=url,callback=self.parse)
    def parse(self, response):
        for error_item in response.css('div.tab-content'):
            yield {
                'user_id': error_item.xpath('.//a[@class="username"]/@href').extract(),
                'user_name': error_item.xpath('.//a[@class="username"]/text()').extract(),
                'user_level': error_item.xpath('.//span[@class="user-level]/text()').re('[^\d]*(\d+)[^\d]*'),
                'course_name': error_item.css('span.question-item-course a::text').extract(),
                'anwered': error_item.xpath('.//div[@class="question-item-answered"]/div[1]/text()').extract(),
                'views': error_item.xpath('.//div[@class="question-item-views"]/div[1]/text()').extract()
            }
