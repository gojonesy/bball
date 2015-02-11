from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'clone.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
	url(r'^', include('teams.urls')),
    url(r'^players/', include('players.urls')),
    url(r'^schedule/', include('schedule.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login', name='login'),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout', name='logout'),
)
