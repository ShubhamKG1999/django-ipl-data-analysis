import csv
from django.core.management.base import BaseCommand
from ipl_data_analysis.models import Match

class Command(BaseCommand):

    def handle(self, *args, **options):
        csv_path = 'csv_files/matches.csv'

        with open(csv_path, 'r') as csv_file:
            reader = csv.reader(csv_file)
            next(reader)

            for row in reader:
                match = Match.objects.create(
                    id=int(row[0]),
                    season=int(row[1]),
                    city=row[2],
                    date=row[3],
                    team1=row[4],
                    team2=row[5],
                    toss_winner=row[6],
                    toss_decision=row[7],
                    result=row[8],
                    dl_applied=bool(row[9]),
                    winner=row[10],
                    win_by_runs=int(row[11]) if row[11] else None,
                    win_by_wickets=int(row[12]) if row[12] else None,
                    player_of_match=row[13],
                    venue=row[14],
                    umpire1=row[15],
                    umpire2=row[16],
                    umpire3=row[17]
                )

        self.stdout.write(self.style.SUCCESS('Matches imported successfully!'))