# Generated by Django 4.2.3 on 2023-07-13 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0016_auto_20210820_1553'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='first name'),
        ),
    ]