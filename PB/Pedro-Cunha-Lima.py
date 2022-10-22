import scrapy

anos = [i for i in range(2015, 2023)]
urls = [f"https://www.camara.leg.br/deputados/178912/votacoes-nominais-plenario/{ano}" for ano in anos]

class PedroCunhaLimaScraper(scrapy.Spider):
    name = 'pedro-cunha-lima-scraper'
    start_urls = urls
    custom_settings = {
        "FEEDS": {
            'pedro-cunha-lima.csv': {
                'format': 'csv'
            }
        }
    }

    def parse(self, response):
        SEL_TABLE = "table"

        for table in response.css(SEL_TABLE):
            SEL_LINHA = "tbody > tr"
            for linha in table.css(SEL_LINHA):
                SEL_URL = "a::href"
                SEL_PAUTA = "a::text"
                SEL_VOTO = "td:nth-child(2)::text"

                yield{
                    'url': linha.css(SEL_URL).extract_first(),
                    'pauta': linha.css(SEL_PAUTA).extract_first(),
                    'voto': linha.css(SEL_VOTO).extract_first()
                }
