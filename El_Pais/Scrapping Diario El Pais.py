#!/usr/bin/env python
# coding: utf-8

# # Diario El Pais - elpais.com.co

# ### Noticias 16-04
# 

# In[1]:


import requests as rq
from bs4 import BeautifulSoup
from datetime import date
import pandas as pd
import numpy as np

datos = {'titulo':[],
       'fecha':[],
       'texto':[],}

ElPais='https://www.elpais.com.co/economia'

col=rq.get(ElPais)
col_soup=BeautifulSoup(col.text, 'lxml')

noticias=col_soup.find('div', attrs={'class':'listing contentNews-listing latest-listing economia-listing category-listing view-list'}).find_all('div', attrs={'class':'listing-item'})    
for noticia in noticias:
    if 'ads-subcategory' not in noticia.get('class'):
        elemento = rq.get('https://www.elpais.com.co/'+str(noticia.a.get('href')))
        elemento_soup = BeautifulSoup(elemento.text, 'lxml')
        datos['titulo'].append(elemento_soup.find('h1', attrs={'class':'title'}).text)
        datos['texto'].append(elemento_soup.find('div', attrs={'class':'article-content'}).text)
        datos['fecha'].append(date.today())           
    else:
        None
ElPais_frame = pd.DataFrame(datos)
ElPais_frame


# In[2]:


#Eliminar noticias con contenido premium
#ElPais_freecontent=ElPais_frame.drop([9, 10, 12 ,16])
#ElPais_freecontent.to_csv(f'{date.today()}.csv')


# In[ ]:





# In[ ]:





# In[ ]:




