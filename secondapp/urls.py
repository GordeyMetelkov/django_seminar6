from django.urls import path
from . import views

urlpatterns = [
    path('coin/<int:count>/', views.coin, name='coin'),
    path('cube/<int:count>', views.cube, name='cube'),
    path('random/<int:count>', views.rand_num, name='rand_num'),
    path('coin_statistic/<int:n>/', views.coin_statistic, name='coin_statistic'),
    path('games/', views.random_games, name='random_games')
]