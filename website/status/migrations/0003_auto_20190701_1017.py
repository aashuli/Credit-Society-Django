# Generated by Django 2.2 on 2019-07-01 04:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('status', '0002_auto_20190701_1016'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='nonteachingstaff',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='account',
            name='teachingstaff',
            field=models.BooleanField(default=False),
        ),
    ]
