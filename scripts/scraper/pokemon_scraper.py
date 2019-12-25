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
            if (table.xpath('tr[1]/td/text()').get() == "Ultra Sun/Ultra Moon Level Up" or
                    table.xpath('tr[1]/td/text()').get() == "Generation VII Level Up" or
                    table.xpath('tr[1]/td/font/text()').get() == "Standard Level Up") and once_standard:
                once_standard = False
                file.write(response.xpath('//*[@class="dextab"]//b/text()').get() + " [")
                for row in table.xpath('tr'):
                    if row.xpath('td[2]//text()').get() is not None and \
                            "Other" not in row.xpath('td[4]/img/@alt').get():
                        file.write("'" + row.xpath('td[2]/a/text()').get() + "' ")
                file.write("]\n")
            elif table.xpath('tr[1]/td/font/text()').get() == "Alola Form Level Up" and once_alola:
                once_alola = False
                file.write(response.xpath('//*[@class="dextab"]//b/text()').get() + " Alola [")
                for row in table.xpath('tr'):
                    if row.xpath('td[2]//text()').get() is not None and \
                            "Other" not in row.xpath('td[4]/img/@alt').get():
                        file.write("'" + row.xpath('td[2]/a/text()').get() + "' ")
                file.write("]\n")
            elif table.xpath('tr[1]/td/text()').get() == "Pre-Evolution Only Moves" and once_pre:
                once_pre = False
                file.write(response.xpath('//*[@class="dextab"]//b/text()').get() + " Pre [")
                for row in table.xpath('tr'):
                    if row.xpath('td[1]//text()').get() is not None and \
                            row.xpath('td[1]//@colspan').get() is None and \
                            "Other" not in row.xpath('td[3]/img/@alt').get():
                        file.write("'" + row.xpath('td[1]/a/text()').get() + "' ")
                file.write("]\n")

        navi_table = '//*[@align="right"]/table[@border="0"]//tr'
        next_page = response.xpath(navi_table + '/td[2]/a/@href').get()
        if "--->" in response.xpath(navi_table + '/td[3]/text()').get():
            return scrapy.Request(
                response.urljoin('https://serebii.net'+next_page),
                callback=self.parse
            )
        file.close()
