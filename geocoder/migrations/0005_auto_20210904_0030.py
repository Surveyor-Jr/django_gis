# Generated by Django 3.2.6 on 2021-09-03 22:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geocoder', '0004_auto_20210904_0020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reversegeocode',
            name='lat',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='reversegeocode',
            name='lon',
            field=models.FloatField(),
        ),
    ]
