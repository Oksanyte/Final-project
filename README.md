### **KINO FILMŲ ANALIZĖ**
#

Baigiamasis darbas atliktas Oksanos Balčiūnaitės ir Giedrės Žalienės.

Projekto tema "Kino filmų analizė".

Pagrindinis šio projekto tikslas - sužinoti populiariausią kino filmų žanrą, 
filmų pasiskirstymą pagal metus, sužinoti kitus statistinius duomenis,
kaip kad ilgiausią ir trumpiausią kino filmą, vidutinius filmų reitingus ir pan.
Nagrinėjami daugiau nei 7600 filmų, periode nuo 1900 metų iki 2021 metų. Kadangi periodas ilgas, 
analizėje laikotarpį suskirstėme į dešimtmečius. 
Šiam projektui atlikti naudojome Python ir CSV files, taip pat Pandas, Matplotlib, Selenium ir
Numpy bibliotekas.

**_main.py_**

Informaciją gavome iš URL https://ww.imdb.com.list/ls503325184/ naudojant BeautifulSoup (bs4)
biblioteką. Surinkome informaciją apie kino filmų pavadinimus, išleidimo metus, žanrus, reitingus ir trukmę.

**_Analize.py_**

Pagrindinis failas kuriame analizavome duomenis. Visos vizualizacijos kontroliuojamos funkcijomis.


Funkcija "Filmų pasiskirstymas pagal dešimtmečius()' parodo, kad daugiausiai išleistų filmų buvo 2000 -2010 metais.


![Image](https://github.com/Oksanyte/Final-project/blob/main/Pictures/filmai_pagal_desimtmecius.png)

Funkcija "Žanrų populiarumas()" atspindi žanrų pasiskirstymą 1900 - 2021 metais ir parodo vienareikšmišką favoritą - "Dramos" žanrą.



![Image](https://github.com/Oksanyte/Final-project/blob/main/Pictures/pop_zanrai.png)

Funkcija "Vidutinė filmo trukmė pagal dešimtmečius()" parodo, kaip keitėsi filmų trukmė bėgant metams.

![Image](https://github.com/Oksanyte/Final-project/blob/main/Pictures/vid_trukme.png)

Funkcija "Filmų trukmių pasiskirstymas()" parodo, kad daugiausiai išleistų filmų mūsų analizuotame periode buvo maždaug 110 - 120 minučių trukmės.



![Image](https://github.com/Oksanyte/Final-project/blob/main/Pictures/trukmiu_pasiskirstymas.png)

_**Išvados**_

Kino filmų analizė parodė, kad periode nuo 1900 metų iki 2021 metų populiariausias kino žanras yra "Drama", vidutinis filmų reitingas yra 7.0, trumpiausias sukurtas filmas analizuojamųjų sąraše yra 11 minučių trukmės,  ilgiausias - 1416 minučių, o vidutinė filmo trukmė 110 minučių, kuri labai neženkliai kito nuo pat 1910 metų. Daugiausiai filmų yra išleista 2000-ųjų metų
pirmajame dešimtmetyje. Analizuojamame periode buvo iš viso 24 žanrai ir kiekvienam filmui buvo priskiriama
ne daugiau kaip trys žanrai.
