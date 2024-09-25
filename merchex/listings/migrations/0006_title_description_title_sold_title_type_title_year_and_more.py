# Generated by Django 5.1.1 on 2024-09-24 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0005_alter_band_genre'),
    ]

    operations = [
        migrations.AddField(
            model_name='title',
            name='description',
            field=models.CharField(default='', max_length=1000),
        ),
        migrations.AddField(
            model_name='title',
            name='sold',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='title',
            name='type',
            field=models.CharField(choices=[('RECORDS', 'Disques'), ('CLOTHING', 'Vetements'), ('POSTERS', 'Affiche'), ('MISCELLANEOUS', 'Divers')], default='', max_length=15),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='title',
            name='year',
            field=models.IntegerField(default=10),
        ),
        migrations.AlterField(
            model_name='title',
            name='name',
            field=models.CharField(default='', max_length=100),
        ),
    ]
