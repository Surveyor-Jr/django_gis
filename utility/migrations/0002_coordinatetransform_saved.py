# Generated by Django 3.2.6 on 2021-08-28 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('utility', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='coordinatetransform',
            name='saved',
            field=models.BooleanField(default=False, verbose_name='Save my data'),
        ),
    ]
