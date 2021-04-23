#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests as rq
from bs4 import BeautifulSoup
from datetime import date
import pandas as pd


# In[2]:


datos = {'titulo':[],
       'fecha':[],
       'texto':[]}
       


# In[3]:


colombia='https://www.eltiempo.com/economia/sectores'
col=rq.get(colombia)
col_soup=BeautifulSoup(col.text, 'lxml')
noticias=col_soup.find('div', attrs={'class':'col2'}).find_all('h3',attrs={'class':'titulo'})
print(len(noticias))
for noticia in noticias[:]:
    print('si')
    elemento=rq.get('https://www.eltiempo.com'+str(noticia.a.get('href')))
    print('https://www.eltiempo.com'+str(noticia.a.get('href')))
    elemento_soup=BeautifulSoup(elemento.text, 'lxml')
    datos['titulo'].append(elemento_soup.find('h1', attrs={'class':'titulo'}).text)
    datos['texto'].append(elemento_soup.find('div', attrs={'class':'col2'}).text)
    datos['fecha'].append(date.today())


# In[36]:


datos


# In[42]:


colombia_noticias = pd.DataFrame(datos)


# In[43]:


colombia_noticias


# In[44]:


colombia_noticias.to_csv(f'{date.today()}.csv')


# In[ ]:




