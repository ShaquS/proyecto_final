from django.urls import path
from game import views


app_name='game'
urlpatterns = [
    path('games', views.GameListView.as_view(), name='game-list'),
    path('game/add/', views.GameCreateView.as_view(), name='game-add'),
    path('game/<int:pk>/detail', views.GameDetailView.as_view(), name='game-detail'),
    path('game/<int:pk>/update', views.GameUpdateView.as_view(), name='game-update'),
    path('game/<int:pk>/delete', views.GameDeleteView.as_view(), name='game-delete'),
]