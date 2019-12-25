import scrapy
import re


class PokemonSpider(scrapy.Spider):
    name_file = open("../../data/resources/unique_moves.json", "r", encoding="utf-8")
    name = "ability_spider"
    line = name_file.readline().rstrip('\n')
    start_urls = ['https://serebii.net/attackdex-swsh/'+line.strip().lower()+'.shtml']

    def parse(self, response):
        file_type = open("../../data/resources/pre-files/pre-unique_moves_types.json", "a+", encoding="utf-8")
        file_cat = open("../../data/resources/pre-files/pre-unique_moves_categories.json", "a+", encoding="utf-8")
        file_pow = open("../../data/resources/pre-files/pre-unique_moves_powers.json", "a+", encoding="utf-8")
        file_pri = open("../../data/resources/pre-files/pre-unique_moves_priority.json", "a+", encoding="utf-8")
        file_cont = open("../../data/resources/pre-files/pre-unique_moves_contact.json", "a+", encoding="utf-8")
        file_st = open("../../data/resources/pre-files/pre-unique_moves_sound.json", "a+", encoding="utf-8")
        file_pt = open("../../data/resources/pre-files/pre-unique_moves_punch.json", "a+", encoding="utf-8")
        file_eff = open("../../data/resources/pre-files/pre-unique_moves_effect.json", "a+", encoding="utf-8")
        file_seff = open("../../data/resources/pre-files/pre-unique_moves_sec-effect.json", "a+", encoding="utf-8")
        for table in response.xpath('//*[@class="dextable"]'):
            if table.xpath('tr[1]/td[1]/b/text()').get() == "Attack Name":
                text = re.findall(r"/.*/(.*?)\..*", table.xpath('tr[2]/td[2]//@href').get())
                file_type.write(self.line + ': ' + ''.join(text) + '\n')
                category = re.findall(r"/.*/(.*?)\..*", table.xpath('tr[2]/td[3]//@href').get())
                file_cat.write(self.line + ': ' + ''.join(category) + '\n')
                text = table.xpath('tr[4]/td[2]//text()').get().replace('\t', '').strip()
                file_pow.write(self.line + ': ' + text + '\n')
                text = table.xpath('tr[6]/td//text()').getall()
                file_eff.write(self.line + ': ' + ''.join(text).replace('\t', '').strip() + '\n')
                if table.xpath('tr[7]/td//text()').get() != "In-Depth Effect:":
                    text = table.xpath('tr[8]/td[1]//text()').getall()
                    file_seff.write(self.line + ': ' + ''.join(text).replace('\t', '').strip() + '\n')
                    if ''.join(category) != "other":
                        text = table.xpath('tr[12]/td[2]//text()').get().replace('\t', '').strip()
                        file_pri.write(self.line + ': ' + text + '\n')
                    else:
                        text = table.xpath('tr[10]/td[2]//text()').get().replace('\t', '').strip()
                        file_pri.write(self.line + ': ' + text + '\n')
                else:
                    text = table.xpath('tr[10]/td[1]//text()').getall()
                    file_seff.write(self.line + ': ' + '[DEPTH]' + ''.join(text).replace('\t', '').strip() + '\n')
                    if ''.join(category) != "other":
                        text = table.xpath('tr[14]/td[2]//text()').get().replace('\t', '').strip()
                        file_pri.write(self.line + ': ' + text + '\n')
                    else:
                        text = table.xpath('tr[12]/td[2]//text()').get().replace('\t', '').strip()
                        file_pri.write(self.line + ': ' + text + '\n')
            elif table.xpath('tr[1]/td[1]/text()').get().replace('\t', '').strip() == "Physical Contact":
                text = '0' if table.xpath('tr[2]/td[1]//text()').get() == 'No' else '1'
                file_cont.write(self.line + ': ' + text + '\n')
                text = '0' if table.xpath('tr[2]/td[2]//text()').get() == 'No' else '1'
                file_st.write(self.line + ': ' + text + '\n')
                text = '0' if table.xpath('tr[2]/td[3]//text()').get() == 'No' else '1'
                file_pt.write(self.line + ': ' + text + '\n')

        self.line = self.name_file.readline().rstrip('\n')
        if self.line != '':
            return scrapy.Request(
                response.urljoin('https://serebii.net/attackdex-swsh/'+self.line.lower().replace(' ', '')+'.shtml'),
                callback=self.parse
            )
        file_type.close()
        file_cat.close()
        file_pow.close()
        file_pri.close()
        file_cont.close()
        file_st.close()
        file_pt.close()
        file_eff.close()
        file_seff.close()
        self.name_file.close()
