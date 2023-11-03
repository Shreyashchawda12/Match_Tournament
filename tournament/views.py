import sys
from django.shortcuts import render, redirect
from django.views.generic import DetailView
from django.views.generic import ListView
from django.db.models import Count, Case, When, IntegerField, F, ExpressionWrapper
from .forms import MatchForm, TeamMatchForm
from .models import Team, TeamMatch, Match
from .logger import logging
from .exception import CustomException

def create_match(request):
    try:
        if request.method == 'POST':
            form = MatchForm(request.POST)
            if form.is_valid():
                logging.info("Creating a new match")
                match = form.save(commit=False)
            
                #Set team1 and team2 using team objects
                team1 = Team.objects.get(id=1)  
                team2 = Team.objects.get(id=2)  
            
                match.team1 = team1
                match.team2 = team2
            
                match.save()
                return redirect('match-list')  
        else:
            form = MatchForm()

        return render(request, 'create_match.html', {'form': form})
    except Exception as e:
            logging.info('Exception at create_match')
            raise CustomException(e,sys)


def create_team_match(request):
    try:
        if request.method == 'POST':
            form = TeamMatchForm(request.POST)
            if form.is_valid():
                form.save()
                logging.info('Redirect to a success page or do something else')
                return redirect('successful')  
        else:
            form = TeamMatchForm()

        return render(request, 'team_match_form.html', {'form': form}) 
    
    except Exception as e:
            logging.info('Exception at create_match')
            raise CustomException(e,sys)

class TeamDetailView(DetailView):
    model = Team
    template_name = 'team_detail.html'
    context_object_name = 'team'
    



class TeamSummaryListView(ListView):
    model = Team
    template_name = 'team_summary_list.html'
    context_object_name = 'team_summary_list'

    def get_queryset(self):
        queryset = Team.objects.all().annotate(
            matches_played=Count('team_matches'),
            matches_won_count=Count(
                Case(When(team_matches__winner=F('id'), then=1), output_field=IntegerField())
            ),
            matches_lost_count=Count(
                Case(When(team_matches__runnerup=F('id'), then=0), default=1, output_field=IntegerField())
            ),
        ).annotate(
            points=ExpressionWrapper(
                F('matches_won_count') * 2, output_field=IntegerField()
            )
        )

        return queryset



    
    


