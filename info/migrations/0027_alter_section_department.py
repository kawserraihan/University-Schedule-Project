# Generated by Django 4.2.3 on 2023-08-28 06:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0026_alter_section_department'),
    ]

    operations = [
        migrations.AlterField(
            model_name='section',
            name='department',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, to='info.dept'),
        ),
    ]