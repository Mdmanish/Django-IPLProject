
from django.urls import path
from . import views

app_name = 'dataset_app'

urlpatterns = [
    path('solution1', views.matches_played_per_year,
         name='matches_played_per_year'),
    path('solution2', views.matches_won_per_team_per_year,
         name='matches_won_per_team_per_year'),
    path('solution3', views.every_team_extra_runs_in_2016,
         name='every_team_extra_runs_in_2016'),
    path('solution4', views.calculate_top_10_eco_bowler,
         name='calculate_top_10_eco_bowler'),
    path('chart1', views.matches_played_per_year_graph,
         name='matches_played_per_year_graph'),
    path('chart2', views.matches_won_per_team_per_year_graph,
         name='matches_won_per_team_per_year_graph'),
    path('chart3', views.every_team_extra_runs_in_2016_graph,
         name='every_team_extra_runs_in_2016_graph'),
    path('chart4', views.calculate_top_10_eco_bowler_graph,
         name='calculate_top_10_eco_bowler_graph')
]
