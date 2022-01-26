from django.shortcuts import render
from bs4 import BeautifulSoup
from rest_framework.views import APIView
from rest_framework.response import Response
from IMDB.models import MovieData
from IMDB.searializers import movieDataRatingSerializers, movieDataSerializers, movieDataTitleSerializers
import requests
# Create your views here.


def home(request):
    # Scrap the Data
    url = "https://www.imdb.com/chart/top?ref_=nv_mv_250"
    site = requests.get(url)
    print(site.status_code)
    soup = BeautifulSoup(site.content, "html.parser")
    table_row_data = soup.find_all('td', class_="titleColumn")

    movies_id = []
    for i in range(len(table_row_data)):
        movies_id.append(table_row_data[i].find('a').get('href'))

    movies_urls = []
    count = 1
    for li in movies_id:
        movies_urls.append(
            f"https://www.imdb.com{li}?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=9703a62d-b88a-4e30-ae12-90fcafafa3fc&pf_rd_r=68K4HZBZAE593S4F7G4E&pf_rd_s=center-1&pf_rd_t=15506&pf_rd_i=top&ref_=chttp_tt_{count}")
        count += 1

    movies_title = []
    movies_rating = []
    movies_release_date = []
    # movies_duration = []
    movies_description = []

    for i in range(len(movies_urls)):
        movies = movies_urls[i]
        movie_site = requests.get(movies)
        movie_soup = BeautifulSoup(
            movie_site.content, "html.parser", from_encoding="iso-8859-1")
        
        movies_title.append(movie_soup.find(
            'div', {"class": "jxsVNt"}).find('h1').text.replace(u'\xa0', u' '))


        movies_rating.append(movie_soup.find(
            'div', {"class": "bmbYRW"}).find('span').text)


        movies_release_date.append(movie_soup.find('div', {"class": "hWHMKr"}).find('a', {"class": "ipc-link"}).text.rstrip('\n'))

        # movies_duration.append(movie_soup.find(
        #     'div', {"class": "hWHMKr"}).find('li', {"class": "ipc-inline-list__item"}).text.strip())

        movies_description.append(movie_soup.find(
            'div', {"class": "frcskz"}).text.strip())


    for i in range(len(movies_urls)):
        movie = MovieData(
            title=movies_title[i], rating=movies_rating[i], relase_date=movies_release_date[i], description=movies_description[i])
        print(movie)
        movie.save()

    return render(request, 'home.html')


class MovieTitle(APIView):
    def get(self, request):
        movie = MovieData.objects.values('title').order_by('title')
        serializer = movieDataTitleSerializers(movie, many=True)
        return Response(serializer.data)


class MovieRating(APIView):
    def get(self, request):
        movie = MovieData.objects.values('rating')
        serializer = movieDataRatingSerializers(movie, many=True)
        return Response(serializer.data)


class MovieReleaseDate(APIView):
    def get(self, request):
        movie = MovieData.objects.values('relase_date').order_by('relase_date')
        serializer = movieDataTitleSerializers(movie, many=True)
        return Response(serializer.data)


class MovieDescription(APIView):
    def get(self, request):
        movie = MovieData.objects.values('description')
        serializer = movieDataTitleSerializers(movie, many=True)
        return Response(serializer.data)


class MovieList(APIView):
    def get(self, request):
        movie = MovieData.objects.all()
        serializer = movieDataSerializers(movie, many=True)
        return Response(serializer.data)
