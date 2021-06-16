from django.db import transaction
from django.http import Http404
from rest_framework import status,filters
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from .models import Actor, Movie, Comment
from .serializers import ActorSerializer, MovieSerializer, CommentSerializer


class CommentAPIView(APIView):
    def get(self, request):
        comments = Comment.objects.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(data=serializer.data)



    def get_object(self, pk):
        try:
            return Comment.objects.get(pk=pk)
        except:
            raise Http404

    def delete(self, request, pk, format=None):
        comment = self.get_object(pk)
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



    def post(self, request):
        serializer = CommentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_204_NO_CONTENT)




class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class MovieViewSet(ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    ordering_fields = ["imdb"]
    search_fields = ["name", "genre"]

    @action(detail=True, methods=['POST'])
    def add_actor(self, request, *args, **kwargs):
        movie = self.get_object()
        with transaction.atomic():
            new_actors = request.data['actor']
            movie.actor.add(new_actors)
            movie.save()
        return Response(status=status.HTTP_204_NO_CONTENT)


    @action(detail=True, methods=['POST'])
    def remove_actor(self, request, *args, **kwargs):
        movie = self.get_object()
        with transaction.atomic():
            change_actor = request.data['actor']
            movie.actor.remove(change_actor)
            movie.save()
        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(detail=True, methods=['GET'])
    def actors(self, request, *args, **kwargs):
        movie = self.get_object()
        actors = movie.actor.all().values()
        data = list(actors)
        return Response(data=data)



class ActorViewSet(ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer

class ActorAPIView(APIView):
    def get(self, request):
        songs = Actor.objects.all()
        serializer = ActorSerializer(songs, many=True)

        return Response(data=serializer.data)

    def post(self, request):
        serializer = ActorSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data)





class MovieAPIView(APIView):
    def get(self, request):
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(data=serializer.data)