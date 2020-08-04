import requests
from bs4 import BeautifulSoup
import csv

soup_objects = []

for i in range(1,100,10):

    base_url = 'https://search.naver.com/search.naver?&where=news&query=%EA%B4%91%EC%A3%BC%20%EC%9D%B8%EA%B3%B5%EC%A7%80%EB%8A%A5%20%EC%82%AC%EA%B4%80%ED%95%99%EA%B5%90&sm=tab_pge&sort=0&photo=0&field=0&reporter_article=&pd=0&ds=&de=&docid=&nso=so:r,p:all,a:all&mynews=0&cluster_rank=33&start='
    start_num = str(i)
    rest_url = '&refresh_start=0'
    # https://search.naver.com/search.naver?sm=mtb_pcv&where=news&query=%EA%B4%91%EC%A3%BC+%EC%9D%B8%EA%B3%B5%EC%A7%80%EB%8A%A5+%EC%82%AC%EA%B4%80%ED%95%99%EA%B5%90&nso=so%3Ar%2Cp%3Aall
    # https://search.naver.com/search.naver?&where=news&query=%EA%B4%91%EC%A3%BC%20%EC%9D%B8%EA%B3%B5%EC%A7%80%EB%8A%A5%20%EC%82%AC%EA%B4%80%ED%95%99%EA%B5%90&sm=tab_pge&sort=0&photo=0&field=0&reporter_article=&pd=0&ds=&de=&docid=&nso=so:r,p:all,a:all&mynews=0&cluster_rank=33&start=11&refresh_start=0
    # https://search.naver.com/search.naver?&where=news&query=%EA%B4%91%EC%A3%BC%20%EC%9D%B8%EA%B3%B5%EC%A7%80%EB%8A%A5%20%EC%82%AC%EA%B4%80%ED%95%99%EA%B5%90&sm=tab_pge&sort=0&photo=0&field=0&reporter_article=&pd=0&ds=&de=&docid=&nso=so:r,p:all,a:all&mynews=0&cluster_rank=46&start=21&refresh_start=0
    # https://search.naver.com/search.naver?&where=news&query=%EA%B4%91%EC%A3%BC%20%EC%9D%B8%EA%B3%B5%EC%A7%80%EB%8A%A5%20%EC%82%AC%EA%B4%80%ED%95%99%EA%B5%90&sm=tab_pge&sort=0&photo=0&field=0&reporter_article=&pd=0&ds=&de=&docid=&nso=so:r,p:all,a:all&mynews=0&cluster_rank=57&start=31&refresh_start=0

    URL = base_url + start_num + rest_url

    response = requests.get(URL)

    soup = BeautifulSoup(response.text, 'html.parser')

    soup_objects.append(soup)

for soup in soup_objects:

    news_section = soup.select(
        'div[id=wrap] > div[id=container] > div[id=content] > div[id=main_pack] > div.news.mynews.section._prs_nws > ul[class=type01] > li'
    )

    for news in news_section:
        a_tag = news.select_one('dl > dt > a')
        news_title = a_tag['title']
        news_link = a_tag['href']
        
        news_data = {
            "title": news_title,
            "hyperlink": news_link
        }

        with open('./naver_news4.csv','a',encoding='utf-8') as csvfile:
            fieldnames = ['title','hyperlink']
            csvwriter = csv.DictWriter(csvfile, fieldnames=fieldnames)
            csvwriter.writerow(news_data)