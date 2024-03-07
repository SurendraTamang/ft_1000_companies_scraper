import scrapy

class FtSpider(scrapy.Spider):
    name = 'ft'

    def start_requests(self):
        year = 2024

        # https://www.ft.com/ft1000-2023
        url = f"https://www.ft.com/ft1000-{year}"
        headers = {
            'authority': 'www.ft.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
            'accept-language': 'en-US,en;q=0.9',
            'sec-ch-ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Brave";v="122"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"macOS"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'sec-gpc': '1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
        }
        yield scrapy.Request(url, self.parse, headers=headers)

    def parse(self, response):
        table_rows = response.xpath("//tbody/tr")
        columns = response.xpath("//thead/tr//text()").extract()
        table_data = []
        for table_row in table_rows:
            table_data_row = table_row.xpath(".//td//text()").extract()
            item = dict(zip(columns, table_data_row))
            yield item

        
