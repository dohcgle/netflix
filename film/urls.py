from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CommentAPIView, CommentViewSet, MovieViewSet, ActorViewSet, ActorAPIView, MovieAPIView

router = DefaultRouter()
router.register('movies', MovieViewSet)
router.register('actors', ActorViewSet)
router.register('comment', CommentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('comments/', CommentAPIView.as_view(), name='comment-list'),
    path('comments/<int:pk>/', CommentAPIView.as_view(), name='comment-delete'),

    # path('movies/', MovieAPIView.as_view(), name='movies'),
    # path('actors/', ActorAPIView.as_view(), name='actors'),
]