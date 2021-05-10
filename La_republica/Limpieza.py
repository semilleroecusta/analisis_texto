
base20 = pd.DataFrame(pd.read_csv('2021-04-20.csv'))
base23 = pd.DataFrame(pd.read_csv('2021-04-23).csv'))
base26 = pd.DataFrame(pd.read_csv('2021-04-26).csv'))
base27 = pd.DataFrame(pd.read_csv('2021-04-27).csv'))
base29 = pd.DataFrame(pd.read_csv('2021-04-29).csv'))
base30 = pd.DataFrame(pd.read_csv('2021-04-30).csv'))
df = (base20.merge(base23,how= 'outer').merge(base26,how= 'outer').merge(base27,how= 'outer').merge(base29,how= 'outer').merge(base30,how= 'outer'))

df_texto = df.drop(['dia','fecha','seccion','Unnamed: 0'],axis=1)
df_texto = df_texto.drop_duplicates('titulo')


