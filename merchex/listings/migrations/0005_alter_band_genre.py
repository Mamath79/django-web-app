# Generated by Django 5.1.1 on 2024-09-24 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0004_band_active_band_biography_band_genre_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='band',
            name='genre',
            field=models.CharField(choices=[('HH', 'Hip Hop'), ('sp', 'Synth Pop'), ('AR', 'Alternative Rock')], max_length=5),
        ),
    ]
