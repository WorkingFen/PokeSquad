import scrapy


class PokemonSpider(scrapy.Spider):
    name_file = open("../../data/resources/unique_abilities.json", "r", encoding="utf-8")
    name = "ability_spider"
    line = name_file.readline().rstrip('\n')
    start_urls = ['https://serebii.net/abilitydex/'+line.strip().lower()+'.shtml']

    def parse(self, response):
        file = open("../../data/resources/unique_abilities_effects.json", "a+", encoding="utf-8")
        for table in response.xpath('//*[@class="dextable"]'):
            if table.xpath('tr[5]/td/text()').get() == "In-Depth Effect:":
                text = table.xpath('tr[6]/td//text()').getall()
                file.write(self.line + ': ' + ''.join(text) + '\n')
            elif table.xpath('tr[3]/td/text()').get() == "Game's Text:":
                text = table.xpath('tr[4]/td//text()').getall()
                file.write(self.line + ': ' + ''.join(text) + '\n')

        self.line = self.name_file.readline().rstrip('\n')
        if self.line != '':
            return scrapy.Request(
                response.urljoin('https://serebii.net/abilitydex/'+self.line.lower().replace(' ', '')+'.shtml'),
                callback=self.parse
            )
        file.close()
        self.name_file.close()
