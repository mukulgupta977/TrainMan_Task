from django.urls import path
from .views import *
from rest_framework.routers import SimpleRouter
from .views import WatchListViewSet

router = SimpleRouter()
router.register(r'watchlist', WatchListViewSet)

urlpatterns = [
    path('list-movies/', MoviesList.as_view()),
    path('fetch-movies/', FetchMovies.as_view()),
]

urlpatterns += router.urls