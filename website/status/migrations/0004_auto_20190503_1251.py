# Generated by Django 2.2 on 2019-05-03 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('status', '0003_auto_20190503_1223'),
    ]

    operations = [
        migrations.RenameField(
            model_name='account',
            old_name='isloantaken',
            new_name='isloanemertaken',
        ),
        migrations.AddField(
            model_name='account',
            name='isloanloantaken',
            field=models.BooleanField(default=False),
        ),
    ]
