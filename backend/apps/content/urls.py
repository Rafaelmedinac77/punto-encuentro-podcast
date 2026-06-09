from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home_data),
    path('episodes/', views.episodes_list),
    path('episodes/<slug:slug>/', views.episode_detail),
    path('guests/', views.guests_list),
    path('articles/', views.articles_list),
    path('subscribe/', views.subscribe),
]
