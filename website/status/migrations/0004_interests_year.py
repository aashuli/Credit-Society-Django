# Generated by Django 2.2 on 2019-07-17 03:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('status', '0003_delete_cal'),
    ]

    operations = [
        migrations.AddField(
            model_name='interests',
            name='year',
            field=models.IntegerField(default=0, null=True),
        ),
    ]