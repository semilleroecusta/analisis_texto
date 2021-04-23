#!/usr/bin/env python
# coding: utf-8

# In[68]:


import requests as rq
from bs4 import BeautifulSoup
from datetime import date
import pandas as pd


# In[69]:


datos = {'titulo':[],
         'dia':[],
       'texto':[]}
       


# In[70]:


colombia='https://www.eltiempo.com/economia/sectores'
col=rq.get(colombia)
col_soup=BeautifulSoup(col.text, 'lxml')
noticias=col_soup.find('div', attrs={'class':'col2'}).find_all('h3',attrs={'class':'titulo'})
print(len(noticias))
if date(2021, 4, 20):
    for noticia in noticias[:]:
        print('si')
        elemento=rq.get('https://www.eltiempo.com'+str(noticia.a.get('href')))
        print('https://www.eltiempo.com'+str(noticia.a.get('href')))
        elemento_soup=BeautifulSoup(elemento.text, 'lxml')
        datos['titulo'].append(elemento_soup.find('h1', attrs={'class':'titulo'}).text)
        datos['texto'].append(elemento_soup.find('div', attrs={'class':'col2'}).text)
        datos['dia'].append(date(2021, 4, 20))
        
else:
    None
 


# In[71]:


datos


# In[72]:


date


# In[73]:


colombia_noticias = pd.DataFrame(datos)


# In[74]:


colombia_noticias


# In[75]:


colombia_noticias.to_csv(f'{date(2021, 4, 20)}.csv')


# In[ ]:




