import scrapy
from wangyi_news.items import WangyiNewsItem


class NewsSpider(scrapy.Spider):
    name = "news"
    allowed_domains = ["news.163.com", "163.com"]
    start_urls = ["https://news.163.com/world/"]

    def parse(self, response):
        hrefs = response.xpath('//div[@class="hidden"]/div/a/@href').extract()
        headers = {
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            # "accept-encoding": "gzip, deflate, br, zstd",
            "accept-language": "zh-CN,zh;q=0.9",
            "cache-control": "max-age=0",
            "cookie": "_ntes_nuid=8a586448b5fe61f28aa3131c1ae73182; BAIDU_SSP_lcr=https://www.baidu.com/link?url=M5FaVmcvI4zqCqfs2-UXlySCK1_83CH50xxDw2oeaB3&wd=&eqid=abd75eac00057c7c0000000567cc19cb; _antanalysis_s_id=1741429254077; UserProvince=%u5168%u56FD; WM_NI=%2FWPe4YhGBlT2pH%2BndQSBo6PgGabXZNmYNzVYYoNdLxPBFq5wqL7g5X%2FkJBp4a2i%2B00tduTkSTKNKZ5eWM0BBLmS%2BqJQNmmSWBP%2Bssfe4ji4K8DQ9q2xu05%2B8ocVxqUuiaWM%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6ee98f372f38f85b8db6efb9a8ea7d54f829b9a87c743baaca384e2599caeb88bc22af0fea7c3b92aed89a086b753ac998e8dd73ab498e58fe75b919ea1d7d36d85bfaeb9d946af87829bd5539bb18285cf74949e8a92b87db394f988b854edb586a3f340a3eea7ccb33cb8bcbbb5ea59989582acd93fa78983d1c14a90b39dccf4429392a38ed25d8290e594f26ea7eca68ab741fc9c9fdaf43abcab00d6aa34adbd9a99f45fb7b7afb8d037e2a3; WM_TID=jREAHoAOp6ZAFEQVABPGIyt2cYCW%2Bh3C; ne_analysis_trace_id=1741430330546; _ntes_origin_from=; s_n_f_l_n3=672f14c9d64ddcbb1741432155797; Hm_lvt_3cf6cca1b315e4d1cef598fe6ec6d83b=1741432670; Hm_lpvt_3cf6cca1b315e4d1cef598fe6ec6d83b=1741432670; HMACCOUNT=A70670DF362C9CAE; pgr_n_f_l_n3=672f14c9d64ddcbb17414315481745886; vinfo_n_f_l_n3=672f14c9d64ddcbb.1.1.1741429199367.1741432122967.1741433926711",
            "priority": "u=0, i",
            "referer": "https://news.163.com/",
            "sec-ch-ua": "\"Chromium\";v=\"134\", \"Not:A-Brand\";v=\"24\", \"Google Chrome\";v=\"134\"",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "\"Windows\"",
            "sec-fetch-dest": "document",
            "sec-fetch-mode": "navigate",
            "sec-fetch-site": "same-site",
            "sec-fetch-user": "?1",
            "upgrade-insecure-requests": "1",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36"
        }
        for url in hrefs:
            yield scrapy.Request(url=url, callback=self.parse_item, headers=headers)
        # yield scrapy.Request(url=hrefs, callback=self.parse_item, headers=headers)

    def parse_item(self, response):
        title = response.xpath('//div/div[contains(@class, "post_main")]/h1/text()').extract()[0]
        p_list = response.xpath(
            '//div/div[contains(@class, "post_main")]/div[@id="content"]/div[contains(@class, "post_body")]//text()').extract()[
                 1:-1:1]
        content = ' '.join(p_list)
        form = response.xpath(
            '//div/div[contains(@class, "post_main")]/div[contains(@class, "post_info")]/a/text()').extract()[0]
        src = response.xpath(
            '//div/div[contains(@class, "post_main")]/div[@id="content"]/div[contains(@class, "post_body")]/p[contains(@class, "f_center")]/img/@src').extract()
        time = \
        response.xpath('//div/div[contains(@class, "post_main")]/div[contains(@class, "post_info")]/text()').extract()[
            0][0:-5:1]

        News = WangyiNewsItem(title=title, time=time, form=form, content=content, src=src)

        yield News
