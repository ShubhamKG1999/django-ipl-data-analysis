from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path('1/', views.matches_per_season, name='matches_per_season'),
    path('2/', views.matches_won_per_team_per_season, name='matches_won_per_team_per_season'),
    path('3/', views.extra_runs_per_team_in_2016, name='extra_runs_per_team_in_2016'),
    path('4/', views.top_10_economical_bowlers_in_2015, name='top_10_economical_bowlers_in_2015'),

    path('1/chart/', views.matches_per_season_chart, name='matches_per_season_chart'),
    path('2/chart/', views.matches_won_per_team_per_season_chart, name='matches_won_per_team_per_season_chart'),
    path('3/chart/', views.extra_runs_per_team_in_2016_chart, name='extra_runs_per_team_in_2016_chart'),
    path('4/chart/', views.top_10_economical_bowlers_in_2015_chart, name='top_10_economical_bowlers_in_2015_chart'),
]