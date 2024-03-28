import requests

from bs4 import BeautifulSoup


def liturgia_diaria():
  #texto que irá retornar
  texto_completo = ''

  url = 'https://liturgia.cancaonova.com/pb/'
  #Retorna se o site está ativo/existe
  response = requests.get(url)

  #Variavel sp que salva todo o HTML do site
  sp = BeautifulSoup(response.text, 'html.parser')

  #Se o sited está ativo:
  if response.status_code == 200:
    #Busca o título e a data (com base no HTML do site)
    titulo = sp.find('title').text
    dia = sp.find(class_ = "dia")
    mes = sp.find(class_ = "mes")
    ano = sp.find(class_ = "ano")

    #Busca as liturgias diárias.
    liturgias = sp.find_all(class_ = 'tab-pane')

    #Adiciona as datas
    texto_completo += titulo + ' ' + dia.text + ' de ' + mes.text + ' de ' + ano.text
    texto_completo += '\n'

    #Para cada classe encontrada da liturgias, ele procura todas as chaves com p
    for liturgia in liturgias:
      versiculos = liturgia.find_all('p')
      texto_completo += '\n'
      #Para cada <p> encontrado ele vai salvar a variavel no texto_completo
      for versiculo in versiculos:
        texto_completo += versiculo.text
        texto_completo += '\n'

    return texto_completo


print(liturgia_diaria())