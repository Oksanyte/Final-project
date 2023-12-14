import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

df = pd.read_csv('baigiamasis1.csv')
df = df.dropna()
df['Metai'] = df['Metai'].str.extract('(\d+)', expand=False).astype(int)
df['Trukmė'] = df['Trukmė'].str.replace(',', '').astype(int)
df['Pavadinimas'] = df['Pavadinimas'].str.replace("'","")
df['Žanras'] = df["Žanras"]
df['Dešimtmetis']  = (df['Metai'] // 10) * 10
df['Šimtmetis'] = (df['Metai'] // 100) * 100


zanru_stulpeliai = df['Žanras'].str.split(', ', expand=True)
df = pd.concat([df, zanru_stulpeliai], axis=1)
df = df.rename(columns={0: 'Žanras1', 1: 'Žanras2', 2: 'Žanras3'})

# print(df)

### STATISTINĖ ANALIZĖ

#Vidutine filmo trukme pagal desimtmecius
avg_length = df.groupby('Dešimtmetis')['Trukmė'].mean().round()
print(f'Vidutinė filmo trukmė (min) pagal dešimtmečius: {avg_length}')


#Reitingų pasiskirstymas pagal dešimtmečius
avg_rating_by_tyear = df.groupby('Dešimtmetis')['Reitingas'].mean().round()
print(f'Filmų reitingas pagal dešimtmetį: {avg_rating_by_tyear}')

#max, min ir avg filmo trukme (atmetus min ir max reiksmes)
max_length = df['Trukmė'].max()
min_length = df['Trukmė'].min()
f_df = df[(df['Trukmė'] != df['Trukmė'].max()) & (df['Trukmė'] != df['Trukmė'].min())]
average_without_minmax = round(f_df['Trukmė'].mean())
print(f'Ilgiausias filmas (min): {max_length}')
print(f'Trumpiausias filmas (min): {min_length}')
print(f'Vidutinė filmo trukmė (min) atmetus mažiausią ir didžiausią reikšmes: {average_without_minmax}')

#populiariausias žanras
top_žanrai = df[['Žanras1', 'Žanras2', 'Žanras3']].stack().value_counts()
print(f'Populiariausias filmų žanras: {top_žanrai}')

#Filmų skaičius pagal dešimtmečius
films_by_tyear = df.groupby('Dešimtmetis')['Pavadinimas'].count()
print(f'Filmų skaičius pagal dešimtmečius: {films_by_tyear}')


#GRAFIKAI

#Filmų pasiskirstymas pagal dešimtmečius
films_by_tyear.plot(kind='bar', color='green')
plt.title('Filmų skaičiaus pasiskirstymas pagal dešimtmečius', fontweight='bold')
plt.xlabel('Dešimtmetis')
plt.ylabel('Filmų skaičius')
plt.xticks(rotation=0)
plt.show()

#Žanrų populiarumas
plt.figure(figsize=(12,8))
top_žanrai.plot(kind='barh')
plt.title('Populiariausi filmų žanrai', fontsize=14, fontweight='bold')
plt.xlabel('Skaičius')
plt.ylabel('Žanras')
plt.show()

#Vidutine filmo trukme pagal desimtmecius
plt.figure(figsize=(8, 8))
labels = [f'{decade} - {length} min' for decade, length in zip(avg_length.index, avg_length)]
plt.pie(avg_length, labels=labels, startangle=90)
plt.title('Vidutinė filmų trukmė pagal dešimtmečius', fontweight='bold')
plt.show()

#Filmų trukmių pasiskirstymas
plt.figure(figsize=(10, 6))
plt.hist(df['Trukmė'], bins=np.logspace(np.log10(min_length), np.log10(max_length), 20), edgecolor='black')
plt.xscale('linear')
plt.yscale('log')
plt.xlabel('Trukmė')
plt.ylabel('Dažnumas (log scale)')
plt.title('Filmų trukmių pasiskirstymas')
plt.grid(True)
plt.show()



