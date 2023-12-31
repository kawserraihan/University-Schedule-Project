# Generated by Django 4.2.5 on 2023-09-06 14:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0028_alter_assign_unique_together_remove_assign_class_id_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='BusDay',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day_of_week', models.PositiveIntegerField(choices=[(0, 'Sunday'), (1, 'Monday'), (2, 'Tuesday'), (3, 'Wednesday'), (4, 'Thursday'), (5, 'Friday'), (6, 'Saturday')], unique=True)),
                ('day_name', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='BusSchedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_of_day', models.TimeField()),
                ('bus_number', models.CharField(max_length=10)),
                ('route_name', models.CharField(max_length=100)),
                ('day', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='info.busday')),
            ],
        ),
    ]
