# my_app/seed_data/hangman.json

from django.db import migrations
from django.core.management import call_command
from my_app.models import HangmanWordBank


def load_seed_data(apps, schema_editor):
    call_command('loaddata', 'my_app/seed_data/hangman.json')


class Migration(migrations.Migration):

    dependencies = [
      ('my_app', '0002_initial')
    ]

    operations = [
        migrations.RunPython(load_seed_data),
    ]