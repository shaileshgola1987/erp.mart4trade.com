import pandas as pd
from django.core.management.base import BaseCommand
from martcrm.models import CountryMaster  # Import CountryMaster model
from decimal import Decimal, InvalidOperation
from django.core.exceptions import ValidationError

class Command(BaseCommand):
    help = 'Import data from CSV to CountryMaster model'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='/home/shivmarb/erp.mart4trade.com/change_log/country_master.csv')

    def handle(self, *args, **options):
        csv_file = options['csv_file']

        # Read CSV file into a pandas DataFrame
        df = pd.read_csv(csv_file, skiprows=1)
        df.columns = df.columns.str.strip()

        # Iterate over DataFrame rows and create CountryMaster objects
        for row in df.itertuples(index=False):
            try:
                # Additional validation for decimal values
                # cr_price = Decimal(str(row[4]))
                # cr_price_old = Decimal(str(row[5]))

                # Check for NaN values in 'isd_code'
                isd_code = row[3].strip() if (pd.notna(row[3]) and row[3].strip() != '') else None

                # Create CountryMaster object
                country_master_instance, created = CountryMaster.objects.get_or_create(
                    country_code=row[0],
                    name=row[1],
                    risk_level=row[2],
                    isd_code=isd_code
                )
            except InvalidOperation as e:
                self.stderr.write(f'Error importing data: {e}')
            except ValidationError as e:
                self.stderr.write(f'Validation error: {e}')

        self.stdout.write(self.style.SUCCESS('Data imported successfully!'))
