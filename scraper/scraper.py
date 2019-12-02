import scrapy


class PokemonSpider(scrapy.Spider):
    name = "poke_spider"
    start_urls = ['https://serebii.net/pokedex-sm/001.shtml']

    def parse(self, response):
        once_standard = True
        once_alola = True
        once_pre = True
        file = open("pre_moves.json", "a+", encoding="utf-8")
        for table in response.xpath('//*[@class="dextable"]'):
            if (table.xpath('tr[1]/td/text()').extract_first() == "Ultra Sun/Ultra Moon Level Up" or
                    table.xpath('tr[1]/td/text()').extract_first() == "Generation VII Level Up" or
                    table.xpath('tr[1]/td/font/text()').extract_first() == "Standard Level Up") and once_standard:
                once_standard = False
                file.write(response.xpath('//*[@class="dextab"]//b/text()').extract_first() + " [")
                for row in table.xpath('tr'):
                    if row.xpath('td[2]//text()').extract_first() is not None and \
                            "Other" not in row.xpath('td[4]/img/@alt').extract_first():
                        file.write("'" + row.xpath('td[2]/a/text()').extract_first() + "' ")
                file.write("]\n")
            elif table.xpath('tr[1]/td/font/text()').extract_first() == "Alola Form Level Up" and once_alola:
                once_alola = False
                file.write(response.xpath('//*[@class="dextab"]//b/text()').extract_first() + " Alola [")
                for row in table.xpath('tr'):
                    if row.xpath('td[2]//text()').extract_first() is not None and \
                            "Other" not in row.xpath('td[4]/img/@alt').extract_first():
                        file.write("'" + row.xpath('td[2]/a/text()').extract_first() + "' ")
                file.write("]\n")
            elif table.xpath('tr[1]/td/text()').extract_first() == "Pre-Evolution Only Moves" and once_pre:
                once_pre = False
                file.write(response.xpath('//*[@class="dextab"]//b/text()').extract_first() + " Pre [")
                for row in table.xpath('tr'):
                    if row.xpath('td[1]//text()').extract_first() is not None and \
                            row.xpath('td[1]//@colspan').extract_first() is None and \
                            "Other" not in row.xpath('td[3]/img/@alt').extract_first():
                        file.write("'" + row.xpath('td[1]/a/text()').extract_first() + "' ")
                file.write("]\n")

        navi_table = '//*[@align="right"]/table[@border="0"]//tr'
        next_page = response.xpath(navi_table + '/td[2]/a/@href').extract_first()
        if "--->" in response.xpath(navi_table + '/td[3]/text()').extract_first():
            return scrapy.Request(
                response.urljoin('https://serebii.net'+next_page),
                callback=self.parse
            )
        file.close()
