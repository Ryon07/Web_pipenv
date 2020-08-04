import requests
import csv
from bs4 import BeautifulSoup

reponse = requests.get('https://movie.naver.com/movie/running/current.nhn')

soup = BeautifulSoup(reponse.text, 'html.parser')

movie_data = soup.select(
    '#content > div.article > div:nth-child(1) > div.lst_wrap > ul > li'
)

final_movie_data = []

for movie in movie_data:
    a_tag = movie.select_one('dl > dt > a')
    movie_title=a_tag.text
    movie_code = a_tag['href'].split('code=')[1]
    movie_list = {
        'title' : movie_title,
        'code' : movie_code
    }

    final_movie_data.append(movie_list)

    print(final_movie_data)