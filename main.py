import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import csv
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/119.0"
}

webdriver_path = "C:/Users/User/Desktop/chromedriver-win64/chromedriver.exe"
service = Service(webdriver_path)
service.start()
driver = webdriver.Chrome(service=service)
data = []


# define website url
URL = f"https://www.imdb.com/list/ls503325184/"
driver.get(URL)

def paspausti():
    load_more = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '.lister-page-next.next-page'))
    )
    driver.execute_script("arguments[0].scrollIntoView();", load_more)
    load_more.click()
    time.sleep(10)
#
# # Atsidarius puslapi yra nuscrolinama i apacia ir palaukiama 3 sekundes
driver.execute_script('window.scrollBy(0, 30000);')
time.sleep(10)
# sukam for cikla siuo atveju 50 kartu ir spaudziamas mygtukas kad uzkrauti daugiau duomenu
for _ in range(1, 3):
    paspausti()


soup = BeautifulSoup(driver.page_source, 'html.parser')
# print(response)
# print(soup)
movies = soup.find_all('div', class_='lister-item-content')
# print(movies)
new_movies_list = []
#
for movie in movies:
    title = movie.find('h3', class_='lister-item-header').text.strip()
    title_text = re.search(r"\n(.+)\n", title).group(1)
    years = movie.find('span', class_='lister-item-year text-muted unbold').text.strip().replace("(", "").replace(")", "")
    length = movie.find('span', class_='runtime').text.strip().replace('min', '')
    genre = movie.find('span', class_='genre').text.strip()
    rating = movie.find('span', class_='ipl-rating-star__rating').text.strip()
    new_movies_list.append({'Pavadinimas': title_text, 'Metai': years, 'Trukmė': length, 'Žanras':genre, 'Reitingas':rating})
#
# # print(new_movies_list)
#
lentele = pd.DataFrame(new_movies_list)
print(lentele)
lentele.to_csv('baigiamasis.csv', index=False)