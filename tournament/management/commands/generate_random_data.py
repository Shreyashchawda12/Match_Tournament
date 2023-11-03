import sys
import random
from django.core.management.base import BaseCommand
from tournament.models import Team, Match, TeamMatch
from datetime import date, timedelta
from tournament.logger import logging
from tournament.exception import CustomException

class Command(BaseCommand):
    help = 'Generate random data for teams, matches, and team matches'

    def handle(self, *args, **options):
        try:
            logging.info('Creating 10 teams')
            countries = [f'Country {i}' for i in range(1, 11)]
            teams = []
            for country in countries:
                team = Team.objects.create(country=country)
                teams.append(team)

            logging.info('Creating 40 unique matches')
            matches = []
            start_date = date(2023, 11, 1)
            for i in range(1, 41):
                match_date = start_date + timedelta(days=i - 1)
                match = Match.objects.create(date=match_date)
                matches.append(match)

            logging.info('Create random TeamMatch instances')
            for i in range(1, 101):  
                match = random.choice(matches)
                team = random.choice(teams)
                batting_score = random.randint(100, 300)
                batting_wickets = random.randint(0, 10)
                batting_overs = random.randint(10, 50)
                TeamMatch.objects.create(match=match, team=team, batting_score=batting_score, batting_wickets=batting_wickets, batting_overs=batting_overs)

            logging.info(self.style.SUCCESS('Random data has been generated successfully.'))
        
        except Exception as e:
            logging.info('Exception at generate_random_data')
            raise CustomException(e,sys)
