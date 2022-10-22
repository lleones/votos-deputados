import scrapy

anos = [str(i) for i in range(2003, 2023)]

urls = [f"https://www.camara.leg.br/deputados/204521/votacoes-nominais-plenario/{ano}" for ano in anos]

class DamiaoFelicianoScraper(scrapy.Spider):
    # Spiders são classes que definem como um determinado site vai ser raspado
    name = 'damiao-feliciano-spider'
    start_urls = urls
    custom_settings = {
        'FEEDS': {
            'damiao-feliciano.csv': {
                'format': 'csv'
            }
        }
    }

    def parse(self, response):
        SEL_SECAO = "table"
        for secao in response.css(SEL_SECAO):
            
            SEL_LINHA = 'tbody > tr'
            for votacao in secao.css(SEL_LINHA):
                SEL_PAUTA = 'a::text'
                SEL_URL = 'a::attr(href)'
                SEL_VOTO = 'td:nth-child(2)::text'
                yield {
                    'pauta': votacao.css(SEL_PAUTA).extract_first(),
                    'url': votacao.css(SEL_URL).extract_first(),
                    'voto': votacao.css(SEL_VOTO).extract_first()                
                }