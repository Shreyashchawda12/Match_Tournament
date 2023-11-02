from django.contrib import admin
from .models import Team, Match, TeamMatch  

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('country',)

@admin.register(Match)
class MatchAdmin(admin.ModelAdmin):
    list_display = ('date',)

@admin.register(TeamMatch)
class TeamMatchAdmin(admin.ModelAdmin):
    list_display = ('team', 'match', 'batting_score', 'batting_wickets', 'batting_overs')


