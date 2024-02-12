import csv
from django.core.management.base import BaseCommand
from martcrm.models.CountryMaster import CountryMaster
from martcrm.models.CityMaster import CityMaster

class Command(BaseCommand):
    help = 'Import data from CSV to CountryStates model'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='Path to the CSV file')

    def handle(self, *args, **options):
        csv_file = options['csv_file']

        with open(csv_file, 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header row if exists

            for row in reader:
                # Assuming the CSV columns are in the same order as model fields
                city,state,country_code = map(str.strip, row)

                try:
                    # Try to fetch the corresponding CountryMaster instance based on the country code
                    country_master_instance = CountryMaster.objects.get(country_code=country_code)
                except CountryMaster.DoesNotExist:
                    # Handle the case where the CountryMaster instance does not exist
                    # You might want to log a warning, create a default instance, or take appropriate action
                    self.stderr.write(f'CountryMaster with country_code {country_code} does not exist.')

                    # You can skip the current row or handle it as needed
                    continue

                # Create the CountryStates instance using the fetched CountryMaster instance
                CityMaster.objects.create(
                    state=state,
                    country_code=country_master_instance,
                    city=city
                    
                )

        self.stdout.write(self.style.SUCCESS('Data imported successfully!'))
