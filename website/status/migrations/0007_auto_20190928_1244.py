# Generated by Django 2.2 on 2019-09-28 07:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('status', '0006_notification_seen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='sender',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='status.Account'),
        ),
    ]
