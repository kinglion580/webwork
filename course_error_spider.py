import scrapy

class CourseErrorSpider(scrapy.Spider):

    name='course-error'

    @property
    def start_url(self):
        url='https://www.shiyanlou.com/questions/?type=course_error&page={}'
        return (url.format(i) for i in range(1,15))

    def parse(self,response):
#for course_error in response.xpath('//ul[contains(@class,"question-items")]'):

        for course_error in response.css('li.course-item'):
                yield {
                "userHref": course_error.css('a.question-item-title::attr(href)').extract_first(),
                "title": course_error.css('a.question-item-title::text').extract_first(),
                "userId": course_error.xpath('//a[@class="username"]/@href').re_first('\d+'),
                "username": course_error.xpath('//a[@class="username"]/text()').extract_first(),
                "username": course_error.xpath('normalize-space(//a[@class="username"]/text())').extract_first(),
                "level": course_error.xpath('//span[@class="user-level"]/text()').re_first('\d+'),
                "date": course_error.css('span.question-item-date::text').extract_first(),
                "courseHref": course_error.css('span.question-item-course a::attr(href)').extract_first(),
                "coursename": course_error.css('span.question-item-course a::text').extract_first(),
                "answered": course_error.xpath('//div[contains(@class,"question-item-rank")]/div/div[1]/text()').extract_first(),
                "viewed": course_error.xpath('//div[contains(@class,"question-item-views")]/div[1]/text()').extract_first()
        }



 
