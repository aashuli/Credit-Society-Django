# Generated by Django 2.2 on 2019-04-23 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('status', '0002_remove_account_sharevalue'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='sharevalue',
            field=models.IntegerField(default=0),
        ),
    ]
