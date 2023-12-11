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

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/119.0"
}

webdriver_path = "C:/Users/User/Desktop/chromedriver-win64/chromedriver.exe"
service = Service(webdriver_path)
service.start()
driver = webdriver.Chrome(service=service)
data = []


# define website url
URL = f"https://www.imdb.com/search/title/?release_date=2020-01-01,2023-12-31&sort=boxoffice_gross_us,desc"
driver.get(URL)
def paspausti():
    load_more = WebDriverWait(driver, 45).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '.ipc-see-more__text > '))
    )
    driver.execute_script("arguments[0].scrollIntoView();", load_more)
    load_more.click()
    time.sleep(4)

# Atsidarius puslapi yra nuscrolinama i apacia ir palaukiama 3 sekundes
driver.execute_script('window.scrollBy(0, 12000);')
time.sleep(3)
# sukam for cikla siuo atveju 50 kartu ir spaudziamas mygtukas kad uzkrauti daugiau duomenu
for i in range(1, 5):
    paspausti()

response = requests.get(URL, headers=headers)
soup = BeautifulSoup(driver.page_source, 'html.parser')
print(response)
print(soup)
movies = soup.find_all('div', class_='sc-53c98e73-4 gOfInm dli-parent')
# print(movies)
new_movies_list = []

for movie in movies:
    title = movie.find('h3', class_='ipc-title__text').text.strip()
    years = movie.find('div', class_='sc-43986a27-7 dBkaPT dli-title-metadata').text.strip()[0:4]
    length = movie.find('div', class_='sc-43986a27-7 dBkaPT dli-title-metadata').text.strip()[4:10]
    certificate = movie.find('div', class_='sc-43986a27-7 dBkaPT dli-title-metadata').text.strip()[10:16]
    # genre = movie.find('span', class_='genre').text.strip()
    rating = movie.find('span', class_= 'ipc-rating-star ipc-rating-star--base ipc-rating-star--imdb ratingGroup--imdb-rating').text.strip()[0:3]
    vote_count = movie.find('span', class_= 'ipc-rating-star ipc-rating-star--base ipc-rating-star--imdb ratingGroup--imdb-rating').text.strip()[5:9].replace('K', '000')
    metascore = movie.find('span', class_='sc-43986a27-11 QigWJ').text.strip()
    votes = movie.find('div', class_='sc-53c98e73-0 kRnqtn').text.replace('Votes', '').strip()
    new_movies_list.append((title, years,length, certificate, rating, vote_count, metascore, votes))



print(new_movies_list)
# df = pd.DataFrame(new_movies_list)
# # print(df)