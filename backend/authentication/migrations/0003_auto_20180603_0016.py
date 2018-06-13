# Generated by Django 2.0 on 2018-06-02 16:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_auto_20180602_2150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='semester',
            field=models.PositiveSmallIntegerField(choices=[(0, '春'), (1, '夏'), (2, '春夏'), (3, '秋'), (4, '冬'), (5, '秋冬'), (6, '短')], default=0, verbose_name='开课学期'),
        ),
        migrations.AlterField(
            model_name='major',
            name='depart',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='major_for', to='authentication.Department', verbose_name='所在院系'),
        ),
        migrations.AlterField(
            model_name='major_class',
            name='major',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='class_name_for', to='authentication.Major', verbose_name='开设专业'),
        ),
    ]
