from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MovieViewSet, ActorViewSet, ActorAPIView, MovieAPIView

router = DefaultRouter()
router.register('movies', MovieViewSet)
router.register('actors', ActorViewSet)

urlpatterns = [
    path('', include(router.urls)),

    # path('movies/', MovieAPIView.as_view(), name='movies'),
    # path('actors/', ActorAPIView.as_view(), name='actors'),
]