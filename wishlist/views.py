from rest_framework.permissions import IsAuthenticated
from rest_framework import generics, viewsets
from .models import Movies, WatchList
from .serializers import MovieSerializer, WatchListSerializer
from Utils.permissions import IsCorrectUser
from rest_framework.views import APIView
from rest_framework.response import Response
from Utils.scrapper import IMBDScrapper


class FetchMovies(APIView):
    permission_classes = [IsAuthenticated]
    def post(self,request):
        try:
            IMBDScrapper(self.request.data.get('url')).imd_movie_picker()
            return Response({"message": "Movies fetched"})
        except Exception as e:
            return Response({"message": "unable to fetch movies"})


class MoviesList(generics.ListCreateAPIView):
    queryset = Movies.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [IsAuthenticated]


class WatchListViewSet(viewsets.ModelViewSet):
    queryset = WatchList.objects.all()
    serializer_class = WatchListSerializer
    permission_classes = [IsAuthenticated & IsCorrectUser]
    http_method_names = ['get', 'post', 'put', 'patch']

    def get_queryset(self):
        queryset = self.queryset
        query_set = queryset.filter(user_id=self.request.user)
        return query_set
