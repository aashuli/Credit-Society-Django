# Generated by Django 2.2 on 2019-07-09 15:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='interests',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sharedividend', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True)),
                ('cddividend', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True)),
                ('fdinterest', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True)),
                ('emerloaninterest', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True)),
                ('longloaninterest', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('accountnumber', models.IntegerField(unique=True)),
                ('name', models.CharField(max_length=50)),
                ('sapid', models.IntegerField(unique=True)),
                ('dateofjoining', models.DateField()),
                ('sharevalue', models.IntegerField(default=0)),
                ('totalinvestment', models.IntegerField(default=0)),
                ('shareamount', models.IntegerField(default=0)),
                ('sharebalance', models.IntegerField(default=0)),
                ('cdamount', models.IntegerField(default=0)),
                ('cdbalance', models.IntegerField(default=0)),
                ('totalamount', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('sharesstartingnumber', models.IntegerField(null=True)),
                ('sharesendingnumber', models.IntegerField(null=True)),
                ('isloantaken', models.BooleanField(default=False)),
                ('isloanemertaken', models.BooleanField(default=False)),
                ('longloanamount', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True)),
                ('longloanprinciple', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True)),
                ('longloanperiod', models.IntegerField(blank=True, default=0, null=True)),
                ('longloaninterestamount', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True)),
                ('longloanbalance', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True)),
                ('longloanemi', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True)),
                ('emerloanamount', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True)),
                ('emerloanprinciple', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True)),
                ('emerloanperiod', models.IntegerField(blank=True, default=0, null=True)),
                ('emerloaninterestamount', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True)),
                ('emerloanbalance', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True)),
                ('emerloanemi', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True)),
                ('fdcapital', models.IntegerField(default=0, null=True)),
                ('fdmaturitydate', models.DateField(null=True)),
                ('teachingstaff', models.BooleanField(default=False)),
                ('nonteachingstaff', models.BooleanField(default=False)),
                ('username', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, unique=True)),
            ],
        ),
    ]
