from datetime import datetime, timedelta, date
import json

from django.shortcuts import get_object_or_404, render_to_response
from django.http import HttpResponse
from django.template import RequestContext
from django.template.loader import render_to_string
from django.conf import settings
from django.views.decorators.cache import cache_page
from django.contrib.auth.decorators import login_required
from django.core.serializers.json import DjangoJSONEncoder

from players.models import Player
from players.utils import get_image_url, calculate_totals, calculate_avgs
from schedule.models import NBA_TEAMS
from teams.models import Team
from teams.utils import calculate_team_totals, calculate_team_avgs

today = datetime.today()
context_data = {}

@login_required(login_url='login')
@cache_page(60*30)
def free_agents(request, num_days=15):
	if request.is_ajax():
		if request.GET.get('filter') == 'seven':
			start_day = today - seven
			new_list = []
			for player in players:
				all_player_stats[player.id] = {}
				total_stats = calculate_totals(player, start_day=start_day, end_day=today)
				avg_stats = calculate_avgs(total_stats)
				all_player_stats[player.id]['name'] = player.name
				all_player_stats[player.id]['nba_team'] = player.nba_team
				all_player_stats[player.id]['position'] = player.position
				all_player_stats[player.id]['stats'] = avg_stats
			new_list.append(render_to_string('free_agents.html', {'all_player_stats': all_player_stats}))
			json = json.dumps(new_list, cls=DjangoJSONEncoder)
			return HttpResponse(json, mimetype='application/json')

	all_player_stats = {}
	players = Player.objects.filter(team__isnull=True)[:50]

	delta = timedelta(days=int(num_days))
	start_day = today - delta

	for player in players:
		all_player_stats[player.id] = {}
		total_stats = calculate_totals(player, start_day=start_day, end_day=today)
		avg_stats = calculate_avgs(total_stats)
		all_player_stats[player.id]['name'] = player.name
		all_player_stats[player.id]['nba_team'] = player.nba_team
		all_player_stats[player.id]['position'] = player.position
		all_player_stats[player.id]['stats'] = avg_stats

	context_data['all_player_stats'] = all_player_stats
	context_data['num_days'] = num_days
	context_data['nba_teams'] = NBA_TEAMS

	return render_to_response('free_agents.html', context_data, 
		context_instance=RequestContext(request))


@login_required(login_url='login')
def add_player(request, player_id, num_days=15):
	player = get_object_or_404(Player, pk=player_id)
	delta = timedelta(days=int(num_days))
	start_day = today - delta
	player_stats = calculate_totals(player, start_day=start_day, end_day=today)
	player_avg_stats = calculate_avgs(player_stats)
	context_data['player_avg_stats'] = player_avg_stats
	context_data['player'] = player

	team = Team.objects.get(owner=request.user.id)
	team_total_stats = calculate_team_totals(team, start_day=start_day, end_day=today)
	team_avg_stats = calculate_team_avgs(team_total_stats)
	team_avg_stats.pop('totals')
	context_data['stats'] = team_avg_stats

	return render_to_response('add_player.html', context_data,
		context_instance=RequestContext(request))


@login_required(login_url='login')
def player_profile(request, player_id, num_days=15):
	player = get_object_or_404(Player, pk=player_id)
	context_data['player'] = player

	url = get_image_url(player.name)
	context_data['image_url'] = url

	delta = timedelta(days=int(num_days))
	start_day = today - delta
	total_stats = calculate_totals(player, start_day=start_day, end_day=today)
	context_data['total_stats'] = total_stats
	
	avg_stats = calculate_avgs(total_stats)
	context_data['avg_stats'] = avg_stats

	return render_to_response('player_profile.html', context_data,
		context_instance=RequestContext(request))
