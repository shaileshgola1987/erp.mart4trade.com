import pandas as pd
from django.core.management.base import BaseCommand
from .martcrm.models.CountryMaster import CountryMaster

class Command(BaseCommand):
    help = 'Import data from CSV to CountryMaster model'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='/home/shivmarb/erp.mart4trade.com/change_log/country_master.csv')

    def handle(self, *args, **options):
        csv_file = options['csv_file']
        
        # Read CSV file into a pandas DataFrame
        df = pd.read_csv(csv_file)

        # Iterate over DataFrame rows and create CountryMaster objects
        for index, row in df.iterrows():
            country_master = CountryMaster(
                country_code=row['country_code'],
                name=row['name'],
                risk_level=row['risk_level'],
                isd_code = row['isd_code'],
                cr_price = row['cr_price'],
                cr_price_old = row['cr_price_old'],
                continent = row ['continent'],
                record_type =row['record_type'],
                im_contact = row ['im_contact'],
                sms_allowed = row ['sms_allowed'],
                neighbour_countries = row['neighbour_countries'],
                name_hi = row['name_hi']
            )
            country_master.save()

        self.stdout.write(self.style.SUCCESS('Data imported successfully!'))