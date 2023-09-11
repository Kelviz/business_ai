from django.urls import path, include
from rest_framework import routers
from .views import GenerateIdeasViewset, AboutViewset, ScrollCardViewset, IdeaListViewset, IdeaDetailViewset


router = routers.DefaultRouter()

router.register('generate-ideas', GenerateIdeasViewset,
                basename="generate-ideas")

router.register('about', AboutViewset, basename='about')

router.register('cards', ScrollCardViewset, basename='cards')

router.register('ideas', IdeaListViewset, basename='ideas')
router.register('detail', IdeaDetailViewset, basename='detail')

urlpatterns = [
    path('', include(router.urls))
]
