#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests as rq
from bs4 import BeautifulSoup
from datetime import date
import pandas as pd
import numpy as np

datos = {'titulo':[],
       'fecha':[],
       'texto':[],
       'seccion':[]}
       
colombia='https://www.larepublica.co/economia'
col=rq.get(colombia)
col_soup=BeautifulSoup(col.text, 'lxml') #entrada a todo el html con "lmxl"
secciones = col_soup.find('div', attrs={'id':'proportional-anchor-1'}).find_all('div',attrs={'class':'col-7 pl-3 pr-3'})

for seccion in secciones[:]: 
    print(seccion.a.get('href'))
    noticias = rq.get(seccion.a.get('href'))
    noticias_sopa = BeautifulSoup(noticias.text,'lxml')
    paginas = noticias_sopa.find('div', attrs={'id':'vue-container'}).find_all('div',attrs={'mb-auto'})
    print(paginas)
    print(len(paginas))
    for pagina in paginas[0:]:
            print('si')
            contenido = rq.get(seccion.a.get('href'))
            contenido_soup = BeautifulSoup(contenido.text, 'lxml')
            datos['titulo'].append(contenido_soup.find('div',attrs={'class':'mb-auto'}).text)
            datos['texto'].append(contenido_soup.find('div',attrs={'class':'html-content'}).text)
            datos['fecha'].append(contenido_soup.find('div',attrs={'class':'d-flex align-items-end'}).text)
            datos['seccion'].append(contenido_soup.find('span',attrs={'class':'kicker economiaSect'}).text)

base=pd.DataFrame(datos)
base.to_csv(f'{date.today()}).csv')

  
   


# In[ ]:





# In[ ]:





# In[ ]:




