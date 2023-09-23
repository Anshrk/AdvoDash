from django.core.management.base import BaseCommand, CommandError
from ...models import Cases, CaseStage, CaseType, Court
import csv

class Command(BaseCommand):
    help = "Initializes the court case types and stuff"

    def handle(self, *args, **options):
        # Add Case Stages
        with open('cases/management/commands/case_types.csv') as file:
            reader = csv.reader(file)
            for line in reader:
                print(line[0])
                CaseType(type=line[0]).save()
        with open('cases/management/commands/courts.csv') as file:
            reader = csv.reader(file)
            for line in reader:
                print(line[0])
                Court(court=line[0]).save()
        with open('cases/management/commands/case_stage.csv') as file:
            reader = csv.reader(file)
            for line in reader:
                print(line[0])
                CaseStage(stage=line[0]).save()
            