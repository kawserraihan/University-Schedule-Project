# Generated by Django 4.2.5 on 2023-09-08 05:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0029_busday_busschedule'),
    ]

    operations = [
        migrations.RenameField(
            model_name='busday',
            old_name='day_name',
            new_name='day',
        ),
        migrations.RemoveField(
            model_name='busday',
            name='day_of_week',
        ),
    ]
