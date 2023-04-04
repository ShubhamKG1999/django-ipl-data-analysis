import csv
from django.core.management.base import BaseCommand
from ipl_data_analysis.models import Delivery, Match

class Command(BaseCommand):

    def handle(self, *args, **options):
        csv_path = 'csv_files/deliveries.csv'

        with open(csv_path, 'r') as csv_file:
            reader = csv.reader(csv_file)
            next(reader)

            for row in reader:
                match_id = int(row[0])
                match = Match.objects.get(id=match_id)

                delivery = Delivery.objects.create(
                    match=match,
                    inning=int(row[1]),
                    batting_team=row[2],
                    bowling_team=row[3],
                    over=int(row[4]),
                    ball=int(row[5]),
                    batsman=row[6],
                    non_striker=row[7],
                    bowler=row[8],
                    is_super_over=int(row[9]),
                    wide_runs=int(row[10]),
                    bye_runs=int(row[11]),
                    legbye_runs=int(row[12]),
                    noball_runs=int(row[13]),
                    penalty_runs=int(row[14]),
                    batsman_runs=int(row[15]),
                    extra_runs=int(row[16]),
                    total_runs=int(row[17]),
                    player_dismissed=row[18],
                    dismissal_kind=row[19],
                    fielder=row[20]
                )

        self.stdout.write(self.style.SUCCESS('Deliveries imported successfully!'))