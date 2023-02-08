class FundoImobiliario:
    def __init__(self, codigo, segmento, cotacao_atual, ffo_yield, dividiend_yield,
                 p_vp, valor_mercado, liquidez, qt_imoveis, preco_m2, aluguel_m2, cap_rate, vacancia_media):
        self.codigo = codigo
        self.segmento = segmento
        self.cotacao_atual = cotacao_atual
        self.ffo_yield = ffo_yield
        self.dividiend_yield = dividiend_yield
        self.p_vp = p_vp
        self.valor_mercado = valor_mercado
        self.liquidez = liquidez
        self.qt_imoveis = qt_imoveis
        self.preco_m2 = preco_m2
        self.aluguel_m2 = aluguel_m2
        self.cap_rate = cap_rate
        self.vacancia_media = vacancia_media

class Estrategia:
    def __init__(self, segmento="", cotacao_atual_minima=0, ffo_yield_minimo=0, dividiend_yield_minimo=0,
                 p_vp_minimo=0, valor_mercado_minimo=0, liquidez_minima=0, qt_minima_imoveis=0,
                 valor_minimo_preco_m2=0, valor_minimo_aluguel_m2=0, valor_minimo_cap_rate=0, maxima_vacancia_media=0):
        self.segmento = segmento
        self.cotacao_atual_minima = cotacao_atual_minima
        self.ffo_yield_minimo = ffo_yield_minimo
        self.dividiend_yield_minimo = dividiend_yield_minimo
        self.p_vp_minimo = p_vp_minimo
        self.valor_mercado_minimo = valor_mercado_minimo
        self.liquidez_minima = liquidez_minima
        self.qt_minima_imoveis = qt_minima_imoveis
        self.valor_minimo_preco_m2 = valor_minimo_preco_m2
        self.valor_minimo_aluguel_m2 = valor_minimo_aluguel_m2
        self.valor_minimo_cap_rate = valor_minimo_cap_rate
        self.maxima_vacancia_media = maxima_vacancia_media

    def aplica_estrategia(self, fundo: FundoImobiliario):
        if fundo.cotacao_atual < self.cotacao_atual_minima:
            return False
        else:
            return True