<<<<<<< HEAD
# Generated by Django 2.1.5 on 2019-04-22 03:39
=======
# Generated by Django 2.1.7 on 2019-04-22 02:49
>>>>>>> upstream/master

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('status', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='sharevalue',
        ),
    ]
