# Generated by Django 4.2.3 on 2023-08-12 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0018_batch_section_day_classdetails'),
    ]

    operations = [
        migrations.AddField(
            model_name='classdetails',
            name='array_name',
            field=models.CharField(default='', max_length=50),
        ),
    ]
