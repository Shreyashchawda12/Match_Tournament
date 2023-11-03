from django import forms
from .models import Match, TeamMatch

class MatchForm(forms.ModelForm):
    class Meta:
        model = Match
        exclude = ['team1', 'team2']

class TeamMatchForm(forms.ModelForm):
    class Meta:
        model = TeamMatch
        fields = ['team', 'match', 'batting_score', 'batting_wickets', 'batting_overs']


