# Generated by Django 2.1.5 on 2019-03-13 03:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('status', '0023_account_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='sapid',
            field=models.IntegerField(default=0),
        ),
    ]
