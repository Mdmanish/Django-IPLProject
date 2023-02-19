from django.core.management.base import BaseCommand
from dataset_app.models import Matches, Deliveries
import csv


class Command(BaseCommand):
    help = 'import booms'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        # Adding matches data in table if already not added
        if not Matches.objects.exists():
            file = open('matches.csv', mode='r')
            csv_data = csv.DictReader(file)

            for line in csv_data:
                models = Matches.objects.create(
                    season=line['season'],
                    city=line['city'],
                    date=line['date'],
                    team1=line['team1'],
                    team2=line['team2'],
                    toss_winner=line['toss_winner'],
                    toss_decision=line['toss_decision'],
                    result=line['result'],
                    dl_applied=line['dl_applied'],
                    winner=line['winner'],
                    win_by_runs=line['win_by_runs'],
                    win_by_wickets=line['win_by_wickets'],
                    player_of_match=line['player_of_match'],
                    venue=line['venue'],
                    umpire1=line['umpire1'],
                    umpire2=line['umpire2'],
                    umpire3=line['umpire3']
                )
                models.save()

        # Adding deliveries data in table if already not added
        if not Deliveries.objects.exists():
            file = open('deliveries.csv', mode='r')
            csv_data = csv.DictReader(file)

            for line in csv_data:
                try:
                    match = Matches.objects.get(id=line['match_id'])
                except Matches.DoesNotExist:
                    match = None

                models = Deliveries.objects.create(
                    match_id=match,
                    inning=line['inning'],
                    batting_team=line['batting_team'],
                    bowling_team=line['bowling_team'],
                    over=line['over'],
                    ball=line['ball'],
                    batsman=line['batsman'],
                    non_striker=line['non_striker'],
                    bowler=line['bowler'],
                    is_super_over=line['is_super_over'],
                    wide_runs=line['wide_runs'],
                    bye_runs=line['bye_runs'],
                    legbye_runs=line['legbye_runs'],
                    noball_runs=line['noball_runs'],
                    penalty_runs=line['penalty_runs'],
                    batsman_runs=line['batsman_runs'],
                    extra_runs=line['extra_runs'],
                    total_runs=line['total_runs'],
                    player_dismissed=line['player_dismissed'],
                    dismissal_kind=line['dismissal_kind'],
                    fielder=line['fielder']
                )
