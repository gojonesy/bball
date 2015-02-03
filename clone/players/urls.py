from django.conf.urls import patterns, url
from teams import urls
from players import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='players_home'),
    url(r'^all_avg/$', views.all_averages, name='all_averages'),
    url(r'^free_agents/$', views.free_agents, name='free_agents'),
    url(r'^(?P<player_id>\d+)/$', views.player_profile, name='player_profile'),
    url(r'^(?P<player_id>\d+)/last_month/$', views.last_month, name='player_last_month'),
    url(r'^(?P<player_id>\d+)/last_fifteen/$', views.last_fifteen, name='player_last_fifteen'),
    url(r'^(?P<player_id>\d+)/last_week/$', views.last_week, name='player_last_week'),
)