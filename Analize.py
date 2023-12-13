import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('baigiamasis1.csv')
df = df.dropna()
df['Metai'] = df['Metai'].str.extract('(\d+)', expand=False).astype(int)
df['Trukmė'] = df['Trukmė'].str.replace(',', '').astype(int)
df['Pavadinimas'] = df['Pavadinimas'].str.replace("'","")
df['Žanras'] = df["Žanras"].str.replace(',', '').replace(' ', '')
df['Dešimtmetis']  = (df['Metai'] // 10) * 10
df['Šimtmetis'] = (df['Metai'] // 100) * 100
# print(df)

### STATISTINĖ ANALIZĖ
#Vidutine filmo trukme pagal desimtmecius
avg_length = df.groupby('Dešimtmetis')['Trukmė'].mean().round()
print(f'Vidutinė filmo trukmė (min) pagal dešimtmečius: {avg_length}')

#Vidutinis reitingas pagal žanrus
avg_rating = df.groupby('Žanras')['Reitingas'].mean().round()
print(f'Vidutinis žanro reitingas: {avg_rating}')

#max ir min filmo trukme
max_length = df['Trukmė'].max()
min_length = df['Trukmė'].min()
print(f'Maksimali filmo trukmė (min): {max_length}')
print(f'Mažiausia filmo trukmė (min): {min_length}')

#populiariausias žanras, filmų pasiskirstymas pagal metus
top_žanras = df['Žanras'].value_counts()
print(f'Populiariausias_žanras: {top_žanras}')
films_by_tyear = df.groupby('Dešimtmetis')['Pavadinimas'].count()
print(f'Filmų pasiskirstymas pagal dešimtmečius: {films_by_tyear}')



#GRAFIKAI

#Filmų reitingų pasiskirstymas
#Žanrų populiarumas
# Reitingų kitimas per metus


# vidutine_trukme.plot(kind='bar')
# plt.title('Vidutinė filmų trukmė pagal dešimtmečius')
# plt.xlabel('Metai')
# plt.ylabel('Vid.trukmė')
# plt.xticks(rotation=0)
# # plt.show()







