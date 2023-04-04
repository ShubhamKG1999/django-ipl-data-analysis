import json
import requests
from django.db.models.expressions import ExpressionWrapper
from django.shortcuts import render
from django.http import JsonResponse
from django.db.models import Count, Sum, F, Case, When, Q, FloatField, Func
from django.db.models.functions import Cast, Trunc, Round
from .models import Match, Delivery


from ipl_data_analysis.models import Match

# Create your views here.
def index(request):
    return render(request, 'index.html')

def matches_per_season(request):
    matches_per_season = Match.objects.values('season').annotate(total_matches=Count('id')).order_by('season')

    result = {'matches_per_season': list(matches_per_season)}

    return JsonResponse(result)

def matches_won_per_team_per_season(request):
    matches_won = Match.objects.values('season', 'winner').annotate(total_wins=Count('winner')).order_by('season', 'winner')

    result = {'matches_won_per_team_per_season': list(matches_won)}

    return JsonResponse(result)

def extra_runs_per_team_in_2016(request):
    extra_runs_per_team_in_2016 = Delivery.objects.filter(match__season=2016).values('bowling_team').annotate(total_extra_runs=Sum('extra_runs'))

    result = {'extra_runs_per_team_in_2016': list(extra_runs_per_team_in_2016)}

    return JsonResponse(result)

def top_10_economical_bowlers_in_2015(request):
    list_of_match_id_in_2015= list(
        Match.objects
        .filter(season=2015)
        .values_list('id', flat=True)
        )
    bowlers_economy = list(
        Delivery.objects.all()
        .filter(match_id__in=list_of_match_id_in_2015)
        .values('bowler')
        .annotate(runs=Cast(
                  Sum('total_runs')-Sum('bye_runs')-Sum('legbye_runs')
                  -Sum('penalty_runs'),output_field=FloatField()),
                  
                  bowlcount=Sum(Case(
                      When(Q(wide_runs__gt=0)| Q(noball_runs__gt=0), then= None),
                      default=1,
                      output_field=FloatField()
                  )),
                  
                  economy_values=ExpressionWrapper(
                    (F('runs') / F('bowlcount'))*6,
                    output_field=FloatField()
        ))
        .annotate(economy=F('economy_values'))
        .values('bowler','economy')
        .order_by(F('economy'))
        [:10])
    
    for item in bowlers_economy:
        item['economy'] = round(item['economy'], 2)

    result = {'top_10_economical_bowlers_in_2015': bowlers_economy}

    return JsonResponse(result)

def matches_per_season_chart(request):

    response = requests.get('http://localhost:8000/1/')
    data = response.json()

    seasons = []
    total_matches = []
    for item in data['matches_per_season']:
        seasons.append(item['season'])
        total_matches.append(item['total_matches'])

    context = {'seasons': seasons, 'total_matches': total_matches}

    return render(request, 'matches_per_season_chart.html', context)

def matches_won_per_team_per_season_chart(request):

    response = requests.get('http://localhost:8000/2/')
    data = response.json()

    chart_data = {}
    seasons = []
    for item in data['matches_won_per_team_per_season']:
        season = item['season']
        winner = item['winner']
        total_wins = item['total_wins']
        if season not in chart_data:
            chart_data[season] = {}
            seasons.append(season)
        chart_data[season][winner] = total_wins

    chart_series = []
    for winner in set([item['winner'] for item in data['matches_won_per_team_per_season']]):
        series_data = []
        for season in seasons:
            if winner in chart_data[season]:
                series_data.append(chart_data[season][winner])
            else:
                series_data.append(0)
        chart_series.append({'name': winner, 'data': series_data})

    print(chart_series[1:])

    context = {'seasons': seasons, 'chart_series': json.dumps(chart_series[1:])}

    return render(request, 'matches_won_per_team_per_season_chart.html', context)

def extra_runs_per_team_in_2016_chart(request):

    response = requests.get('http://localhost:8000/3/')
    data = response.json()

    teams = []
    extra_runs = []
    for item in data['extra_runs_per_team_in_2016']:
        teams.append(item['bowling_team'])
        extra_runs.append(item['total_extra_runs'])

    context = {'teams': teams, 'extra_runs': extra_runs}

    return render(request, 'extra_runs_per_team_in_2016_chart.html', context)

def top_10_economical_bowlers_in_2015_chart(request):

    response = requests.get('http://localhost:8000/4/')
    data = response.json()

    bowlers = []
    economy = []
    for item in data['top_10_economical_bowlers_in_2015']:
        bowlers.append(item['bowler'])
        economy.append(item['economy'])

    context = {'bowlers': bowlers, 'economy': economy}

    return render(request, 'top_10_economical_bowlers_in_2015_chart.html', context)