import requests as rq
from bs4 import BeautifulSoup
from datetime import date
import pandas as pd


datos = {'titulo':[],
       'fecha':[],
       'texto':[]}


portafolio='https://www.portafolio.co/economia'
port = rq.get(portafolio)
port_sopa = BeautifulSoup(port.text, 'lxml')
noticias = port_sopa.find_all('div', attrs={'class':'secondary-board modules'})[1].find_all('div',attrs={'class':'listing-item'})
for noticia in noticias[:-1]:
    print(noticia.a.get('href'))
    elemento = rq.get('https://www.portafolio.co'+noticia.a.get('href'))
    elemento_sopa = BeautifulSoup(elemento.text, 'lxml')
    datos['titulo'].append(elemento_sopa.find('h1', attrs={'itemprop':'headline'}).text)
    datos['fecha'].append(date.today())
    datos['texto'].append(elemento_sopa.find('div', attrs={'class':'article-content'}).text)


portafolio_noticias = pd.DataFrame(datos)


portafolio_noticias


portafolio_noticias.to_csv(f'{date.today()}.csv')



