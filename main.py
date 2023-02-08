import requests
from bs4 import BeautifulSoup
import locale

from modelos import FundoImobiliario

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')


def trata_porcentagem(porcentagem_str):
    return locale.atof(porcentagem_str.split('%')[0])


def trata_decimal(decimal_str):
    return locale.atof(decimal_str)


headers = {'User-Agent': 'Mozilla/5.0'}

response = requests.get('https://source.android.com/docs/security/bulletin/2023-02-01?hl=pt-br', headers=headers)

soup = BeautifulSoup(response.text, 'html.parser')

rows = soup.find_all("table")

teste = {}
tds = []

for row in rows[0]:
    trow = row.find_all("tr")
    for tr in trow:
        print(tr.text.split(" "))




pass
# rows = soup.find(class_='leagues--live contest--leagues')
# mydivs = soup.find_all('div', 'sportName basketball')
# mydivs = soup.find_all("div", class_="devsite-table-wrapper")


#
# for row in rows:
#     fundo_data = row.find_all('td')
#     codigo = fundo_data[0].text
#     segmento = fundo_data[1].text
#     cotacao = trata_decimal(fundo_data[2].text)
#     ffo_yield = trata_porcentagem(fundo_data[3].text)
#     dividiend_yield = trata_porcentagem(fundo_data[4].text)
#     p_vp = trata_decimal(fundo_data[5].text)
#     valor_mercado = trata_decimal(fundo_data[6].text)
#     liquidez = trata_decimal(fundo_data[7].text)
#     qt_imoveis = int(fundo_data[8].text)
#     preco_m2 = trata_decimal(fundo_data[9].text)
#     aluguel_m2 = trata_decimal(fundo_data[10].text)
#     cap_rate = trata_porcentagem(fundo_data[11].text)
#     vacancia_media = trata_porcentagem(fundo_data[12].text)
#
#     fundo_imobiliario = FundoImobiliario(
#         codigo,
#         segmento,
#         cotacao,
#         ffo_yield,
#         dividiend_yield,
#         p_vp,
#         valor_mercado,
#         liquidez,
#         qt_imoveis,
#         preco_m2,
#         aluguel_m2,
#         cap_rate,
#         vacancia_media,
#     )
