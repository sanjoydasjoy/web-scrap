from django.urls import path
from .views import scrape

urlpatterns = [
    path('', scrape, name='scrape'),
    path('newest/', scrape, name='scrape-newest'),
    path('news/', scrape, name='scrape-news'),
    path('from/', scrape, name='scrape-from'),
]