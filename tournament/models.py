from django.db import models

# Create your models here.

class Team(models.Model):
    country = models.CharField(max_length=3, unique=True)
    @property
    def matches_played(self):
        # Count the number of matches related to this team using the reverse relationship
        return self.matches_as_team1.count() + self.matches_as_team2.count()
    @property
    def matches_won(self):
        # Count the number of matches won by the team
        return self.matches_won.count()
    @property
    def matches_lost(self):
        # Count the number of matches lost by the team
        return self.matches_played() - self.matches_won()

    
class Match(models.Model):
    date = models.DateField()
    team1 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='matches_as_team1')
    team2 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='matches_as_team2')
    winner = models.ForeignKey(Team, on_delete=models.CASCADE, null=True, blank=True, related_name='matches_won')
    runnerup = models.ForeignKey(Team, on_delete=models.CASCADE, null=True, blank=True, related_name='matches_lost')
    
 
    
    
class TeamMatch(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='team_matches')
    match = models.ForeignKey(Match, on_delete=models.CASCADE, related_name='team_matches')
    batting_score = models.IntegerField()
    batting_wickets = models.IntegerField()
    batting_overs = models.IntegerField()
