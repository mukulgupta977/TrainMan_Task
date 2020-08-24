import requests
from bs4 import BeautifulSoup
import random
from wishlist.models import Movies
from django.db.utils import IntegrityError


class IMBDScrapper:

    def __init__(self, website_url):
        self.website_url = website_url

    def get_imd_movies(self, url):
        page = requests.get(url)
        soup = BeautifulSoup(page.text, 'html.parser')
        movies = soup.find_all("td", class_="titleColumn")
        random.shuffle(movies)
        return movies

    def get_imd_summary(self, url):
        movie_page = requests.get(url)
        soup = BeautifulSoup(movie_page.text, 'html.parser')
        return soup.find("div", class_="summary_text").contents[0].strip()

    def get_imd_movie_info(self, movie):
        movie_title = movie.a.contents[0]
        movie_year = movie.span.contents[0]
        movie_url = 'http://www.imdb.com' + movie.a['href']
        return movie_title, movie_year, movie_url

    def imd_movie_picker(self):
        ctr = 0
        for movie in self.get_imd_movies(self.website_url):
            movie_title, movie_year, movie_url = self.get_imd_movie_info(movie)
            movie_summary = self.get_imd_summary(movie_url)
            try:
                record = Movies.objects.create(title=movie_title, year=str(movie_year).strip('[(,)]'), summary=movie_summary)
            except IntegrityError:
                record = Movies.objects.filter(title=movie_title, year=str(movie_year).strip('[(,)]'))[0]
                record.summary = movie_summary
                record.save()

            ctr = ctr + 1
            if ctr == 10:
                break


