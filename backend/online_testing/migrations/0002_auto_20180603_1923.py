# Generated by Django 2.0.5 on 2018-06-03 11:23

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('online_testing', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paper',
            name='deadline',
            field=models.DateTimeField(default=datetime.datetime(2018, 6, 3, 11, 23, 16, 950786, tzinfo=utc), verbose_name='结束时间'),
        ),
        migrations.AlterField(
            model_name='paper',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 6, 3, 11, 23, 16, 950786, tzinfo=utc), verbose_name='开始时间'),
        ),
    ]
