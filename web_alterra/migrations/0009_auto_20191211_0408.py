# Generated by Django 3.0 on 2019-12-11 04:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_alterra', '0008_auto_20191211_0353'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='date_post',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 11, 4, 8, 22, 70149)),
        ),
    ]
