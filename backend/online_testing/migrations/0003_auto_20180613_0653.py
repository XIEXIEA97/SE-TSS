# Generated by Django 2.0 on 2018-06-13 06:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('online_testing', '0002_auto_20180612_1354'),
    ]

    operations = [
        migrations.AlterField(
            model_name='examination',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 6, 13, 6, 53, 58, 695033), verbose_name='开始时间'),
        ),
        migrations.AlterField(
            model_name='paper',
            name='deadline',
            field=models.DateTimeField(default=datetime.datetime(2018, 6, 13, 6, 53, 58, 693189), verbose_name='结束时间'),
        ),
        migrations.AlterField(
            model_name='paper',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 6, 13, 6, 53, 58, 693153), verbose_name='开始时间'),
        ),
    ]
