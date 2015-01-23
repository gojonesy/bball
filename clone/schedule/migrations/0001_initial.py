# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField()),
                ('tipoff', models.DateTimeField()),
                ('home_team', models.CharField(max_length=25, verbose_name='Home Team', choices=[(b'ATL', b'Atlanta Hawks'), (b'BRK', b'Brooklyn Nets'), (b'BOS', b'Boston Celtics'), (b'CHO', b'Charlotte Hornets'), (b'CHI', b'Chicago Bulls'), (b'CLE', b'Cleveland Cavaliers'), (b'DAL', b'Dallas Mavericks'), (b'DEN', b'Denver Nuggets'), (b'DET', b'Detroit Pistons'), (b'GSW', b'Golden State Warriors'), (b'HOU', b'Houston Rockets'), (b'IND', b'Indiana Pacers'), (b'LAC', b'Los Angeles Clippers'), (b'LAL', b'Los Angeles Lakers'), (b'MEM', b'Memphis Grizzlies'), (b'MIA', b'Miami Heat'), (b'MIN', b'Minnesota Timberwolves'), (b'MIL', b'Milwaukee Bucks'), (b'NOP', b'New Orleans Pelicans'), (b'NYK', b'New York Knicks'), (b'OKC', b'Oklahoma City Thunder'), (b'ORL', b'Orlando Magic'), (b'PHI', b'Philadelphia 76ers'), (b'PHO', b'Phoenix Suns'), (b'POR', b'Portland TrailBlazers'), (b'SAS', b'San Antonio Spurs'), (b'SAC', b'Sacramento Kings'), (b'TOR', b'Toronto Raptors'), (b'UTA', b'Utah Jazz'), (b'WAS', b'Washington Wizards'), (b'FA', b'Free Agent')])),
                ('away_team', models.CharField(max_length=25, verbose_name='Away Team', choices=[(b'ATL', b'Atlanta Hawks'), (b'BRK', b'Brooklyn Nets'), (b'BOS', b'Boston Celtics'), (b'CHO', b'Charlotte Hornets'), (b'CHI', b'Chicago Bulls'), (b'CLE', b'Cleveland Cavaliers'), (b'DAL', b'Dallas Mavericks'), (b'DEN', b'Denver Nuggets'), (b'DET', b'Detroit Pistons'), (b'GSW', b'Golden State Warriors'), (b'HOU', b'Houston Rockets'), (b'IND', b'Indiana Pacers'), (b'LAC', b'Los Angeles Clippers'), (b'LAL', b'Los Angeles Lakers'), (b'MEM', b'Memphis Grizzlies'), (b'MIA', b'Miami Heat'), (b'MIN', b'Minnesota Timberwolves'), (b'MIL', b'Milwaukee Bucks'), (b'NOP', b'New Orleans Pelicans'), (b'NYK', b'New York Knicks'), (b'OKC', b'Oklahoma City Thunder'), (b'ORL', b'Orlando Magic'), (b'PHI', b'Philadelphia 76ers'), (b'PHO', b'Phoenix Suns'), (b'POR', b'Portland TrailBlazers'), (b'SAS', b'San Antonio Spurs'), (b'SAC', b'Sacramento Kings'), (b'TOR', b'Toronto Raptors'), (b'UTA', b'Utah Jazz'), (b'WAS', b'Washington Wizards'), (b'FA', b'Free Agent')])),
                ('home_points', models.IntegerField(default=0)),
                ('away_points', models.IntegerField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Season',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
