import csv
import datetime
import os

from django.conf import settings
from django.core.management.base import BaseCommand

from ...models import Art

class Command(BaseCommand):
    help = 'Backup Art data'

    def handle(self, *args, **options):
        date = datetime.date.today().strftime('%Y%m%d')

        file_path = settings.BACKUP_PATH + 'art' + date + '.csv'

        os.makedirs(settings.BACKUP_PATH, exist_ok=True)

        with open(file_path, 'w') as file:
            writer = csv.writer(file)

            header = [field.name for field in Art._meta.fields]
            writer.writerow(header)

            arts = Art.objects.all()

            for art in arts:
                writer.writerow(
                    [
                        art.title,
                        str(art.date),
                        str(art.image),
                        str(art.description),
                    ]
                )

            files = os.listdir(settings.BACKUP_PATH)
            if len(files) >= settings.NUM_SAVED_BACKUP:
                files.sort()
                os.remove(settings.BACKUP_PATH + files[0])
