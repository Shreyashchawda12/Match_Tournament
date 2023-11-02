from django.db import models

# Create your models here.

class Team(models.Model):
    country = models.CharField(max_length=3, unique=True)
    
    def matches_played(self):
        # Count the number of matches related to this team using the reverse relationship
        return self.team_matches.count()
    
    def matches_won(self):
        # Count the number of matches won by the team using the reverse relationship
        return self.team_matches.filter(won=True).count()
    
    def matches_lost(self):
        # Count the number of matches lost by the team using the reverse relationship
        return self.team_matches.filter(won=False).count()
    
class Match(models.Model):
    date = models.DateField()
  
 
    
    
class TeamMatch(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='team_matches')
    match = models.ForeignKey(Match, on_delete=models.CASCADE, related_name='team_matches')
    batting_score = models.IntegerField()
    batting_wickets = models.IntegerField()
    batting_overs = models.IntegerField()
