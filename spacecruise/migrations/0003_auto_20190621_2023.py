# Generated by Django 2.2 on 2019-06-21 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spacecruise', '0002_auto_20190621_1307'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tourists',
            name='list_of_flights',
            field=models.ManyToManyField(blank=True, related_name='flights', to='spacecruise.Flights'),
        ),
    ]
