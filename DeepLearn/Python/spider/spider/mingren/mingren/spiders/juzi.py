import scrapy


class JuziSpider(scrapy.Spider):
    name = "juzi"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["https://quotes.toscrape.com/tag/humor/"]

    def parse(self, response):
        quote_div_list = response.xpath('//div/div[@class="col-md-8"]/div[@class="quote"]')
        # print(quote_div_list)
        for quote in quote_div_list:
            text = quote.xpath('.//span[@class="text"]/text()').get()
            author = quote.xpath('.//span/small[@class="author"]/text()').get()
            yield {
                'text': text,
                'author': author
            }

        next_page = response.xpath('//nav//a/@href').get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)
        # for quote in response.css("div.quote"):
        #     yield {
        #         "author": quote.xpath("span/small/text()").get(),
        #         "text": quote.css("span.text::text").get(),
        #     }
        #
        # next_page = response.css('li.next a::attr("href")').get()
        # if next_page is not None:
        #     yield response.follow(next_page, self.parse)
