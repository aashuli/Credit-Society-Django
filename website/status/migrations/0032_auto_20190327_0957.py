# Generated by Django 2.1.7 on 2019-03-27 04:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('status', '0031_auto_20190327_0953'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='department',
        ),
        migrations.DeleteModel(
            name='Department',
        ),
    ]
