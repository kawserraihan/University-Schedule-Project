# Generated by Django 4.2.5 on 2023-10-05 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0032_alter_classdetails_classend_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='busschedule',
            name='time_of_day',
            field=models.CharField(default=None, max_length=5),
        ),
    ]
