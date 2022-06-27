from django.urls import path
from music import views


app_name='music'
urlpatterns = [
    path('musics', views.MusicListView.as_view(), name='music-list'),
    path('music/add/', views.MusicCreateView.as_view(), name='music-add'),
    path('music/<int:pk>/detail', views.MusicDetailView.as_view(), name='music-detail'),
    path('music/<int:pk>/update', views.MusicUpdateView.as_view(), name='music-update'),
    path('music/<int:pk>/delete', views.MusicDeleteView.as_view(), name='music-delete'),
]