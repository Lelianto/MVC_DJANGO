# Generated by Django 3.0 on 2019-12-10 14:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_alterra', '0002_auto_20191210_1004'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='date_post',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 10, 14, 2, 13, 574613)),
        ),
    ]