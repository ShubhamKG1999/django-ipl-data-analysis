from django.db import models

# Create your models here.
class Match(models.Model):
    id = models.IntegerField(primary_key=True)
    season = models.IntegerField()
    city = models.CharField(max_length=255, null=True, blank=True)
    date = models.DateField()
    team1 = models.CharField(max_length=255)
    team2 = models.CharField(max_length=255)
    toss_winner = models.CharField(max_length=255)
    toss_decision = models.CharField(max_length=255)
    result = models.CharField(max_length=255)
    dl_applied = models.BooleanField()
    winner = models.CharField(max_length=255, null=True, blank=True)
    win_by_runs = models.IntegerField(null=True, blank=True)
    win_by_wickets = models.IntegerField(null=True, blank=True)
    player_of_match = models.CharField(max_length=255, null=True, blank=True)
    venue = models.CharField(max_length=255)
    umpire1 = models.CharField(max_length=255, null=True, blank=True)
    umpire2 = models.CharField(max_length=255, null=True, blank=True)
    umpire3 = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        verbose_name_plural = "matches"

class Delivery(models.Model):
    match = models.ForeignKey(Match, on_delete=models.CASCADE)
    inning = models.IntegerField()
    batting_team = models.CharField(max_length=255)
    bowling_team = models.CharField(max_length=255)
    over = models.IntegerField()
    ball = models.IntegerField()
    batsman = models.CharField(max_length=255)
    non_striker = models.CharField(max_length=255)
    bowler = models.CharField(max_length=255)
    is_super_over = models.BooleanField()
    wide_runs = models.IntegerField()
    bye_runs = models.IntegerField()
    legbye_runs = models.IntegerField()
    noball_runs = models.IntegerField()
    penalty_runs = models.IntegerField()
    batsman_runs = models.IntegerField()
    extra_runs = models.IntegerField()
    total_runs = models.IntegerField()
    player_dismissed = models.CharField(max_length=255, null=True, blank=True)
    dismissal_kind = models.CharField(max_length=255, null=True, blank=True)
    fielder = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        verbose_name_plural = "deliveries"