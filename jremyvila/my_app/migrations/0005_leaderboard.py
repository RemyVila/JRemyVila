from django.db import migrations, models
from my_app.models import Leaderboard


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0004_userprofile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Leaderboard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=30)),
                ('wins', models.IntegerField()),
                ('losses', models.IntegerField()),
            ],
        ),
    ]
