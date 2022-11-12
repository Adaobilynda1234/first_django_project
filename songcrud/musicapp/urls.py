from django.urls import path

from .views import songList,songDetail,ArtisteList,ArtisteDetail

urlpatterns =[
    path("song/<int:pk>/" ,songDetail.as_view(),name ="song_detail"),
    path("song/",songList.as_view(),name ="song_list"),
    path("artiste/<int:pk>/" ,ArtisteDetail.as_view(),name ="artiste_detail"),
    path("artiste/",ArtisteList.as_view(),name ="artiste_list"),
]