# Generated by Django 3.0 on 2019-12-10 14:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_alterra', '0006_auto_20191210_1408'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='date_post',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 10, 14, 8, 41, 217019)),
        ),
    ]
