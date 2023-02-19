from django.shortcuts import render, reverse
from django.http import JsonResponse
from django.db.models import Count, Sum, FloatField
from django.db.models.functions import Cast
from .models import Matches, Deliveries

# Number of matches played per year for all the years in IPL.


def matches_played_per_year(request):
    no_of_matches_played_every_year = Matches.objects.values(
        'season').annotate(total_match_played=Count('season'))
    return JsonResponse(list(no_of_matches_played_every_year), safe=False)

# Number of matches won per team per year in IPL.


def matches_won_per_team_per_year(request):
    no_of_matches_won_per_team_per_year = Matches.objects.values(
        'season', 'winner').annotate(count=Count('winner')).order_by('season', 'winner')
    return JsonResponse(list(no_of_matches_won_per_team_per_year), safe=False)


# Extra runs conceded per team in the year 2016


def every_team_extra_runs_in_2016(request):
    extra_runs_of_every_team = Deliveries.objects.filter(
        match_id__season=2016).values('bowling_team').annotate(Sum('extra_runs'))
    return JsonResponse(list(extra_runs_of_every_team), safe=False)

# Top 10 economical bowlers in the year 2015


def calculate_top_10_eco_bowler(request):
    top_10_eco_bowler = Deliveries.objects.filter(match_id__season=2015, is_super_over=0).values(
        'bowler').annotate(economic_rate=(Cast((Sum('total_runs') * 6.0) / Count('total_runs'), FloatField()))).order_by('economic_rate')[:10]
    return JsonResponse(list(top_10_eco_bowler), safe=False)


def matches_played_per_year_graph(request):
    json_context = {
        'question_url': reverse('dataset_app:matches_played_per_year'),
        'title': 'Number of matches played per year for all the years in IPL.',
        'xAxis': 'season',
        'yAxis': 'total_match_played',
        'xLable': 'season',
        'yLable': 'total_match_played',
        'graphType': 'bar'
    }
    return render(request, template_name='dataset_app/index.html', context=json_context)


def matches_won_per_team_per_year_graph(request):
    json_context = {
        'question_url': reverse('dataset_app:matches_won_per_team_per_year'),
        'title': 'Number of matches won per team per year in IPL.',
        'xAxis': 'winner',
        'yAxis': 'count',
        'xLable': 'winner',
        'yLable': 'count',
        'graphType': 'groupedBar'
    }
    return render(request, template_name='dataset_app/index.html', context=json_context)


def every_team_extra_runs_in_2016_graph(request):
    json_context = {
        'question_url': reverse('dataset_app:every_team_extra_runs_in_2016'),
        'title': 'Extra runs conceded per team in the year 2016',
        'xAxis': 'bowling_team',
        'yAxis': 'extra_runs__sum',
        'xLable': 'bowling_team',
        'yLable': 'extra_runs__sum',
        'graphType': 'bar'
    }
    return render(request, template_name='dataset_app/index.html', context=json_context)


def calculate_top_10_eco_bowler_graph(request):
    json_context = {
        'question_url': reverse('dataset_app:calculate_top_10_eco_bowler'),
        'title': 'Top 10 economical bowlers in the year 2015',
        'xAxis': 'bowler',
        'yAxis': 'economic_rate',
        'xLable': 'bowler',
        'yLable': 'economic_rate',
        'graphType': 'bar'
    }
    return render(request, template_name='dataset_app/index.html', context=json_context)
