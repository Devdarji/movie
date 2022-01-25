from django.urls import path
from IMDB.views import MovieList, home, MovieTitle, MovieRating, MovieDuration, MovieDescription, MovieReleaseDate

app_name = 'IMDB'
urlpatterns = [
    path('', home, name="home"),
    path('movies/title/', MovieTitle.as_view(), name="title"),
    path('movies/rating/', MovieRating.as_view(), name="rating"),
    path('movies/release-date/', MovieReleaseDate.as_view(), name="release_date"),
    path('movies/duration/', MovieDuration.as_view(), name="duration"),
    path('movies/description/', MovieDescription.as_view(), name="movieList"),
    path('movies/', MovieList.as_view(), name="movieList"),
]
