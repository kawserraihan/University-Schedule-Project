# Generated by Django 4.2.4 on 2023-09-01 04:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0027_alter_section_department'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='assign',
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name='assign',
            name='class_id',
        ),
        migrations.RemoveField(
            model_name='assign',
            name='course',
        ),
        migrations.RemoveField(
            model_name='assign',
            name='teacher',
        ),
        migrations.RemoveField(
            model_name='assigntime',
            name='assign',
        ),
        migrations.RemoveField(
            model_name='attendance',
            name='attendanceclass',
        ),
        migrations.RemoveField(
            model_name='attendance',
            name='course',
        ),
        migrations.RemoveField(
            model_name='attendance',
            name='student',
        ),
        migrations.RemoveField(
            model_name='attendanceclass',
            name='assign',
        ),
        migrations.DeleteModel(
            name='AttendanceRange',
        ),
        migrations.AlterUniqueTogether(
            name='attendancetotal',
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name='attendancetotal',
            name='course',
        ),
        migrations.RemoveField(
            model_name='attendancetotal',
            name='student',
        ),
        migrations.AlterUniqueTogether(
            name='marks',
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name='marks',
            name='studentcourse',
        ),
        migrations.AlterUniqueTogether(
            name='marksclass',
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name='marksclass',
            name='assign',
        ),
        migrations.RemoveField(
            model_name='student',
            name='class_id',
        ),
        migrations.RemoveField(
            model_name='student',
            name='user',
        ),
        migrations.AlterUniqueTogether(
            name='studentcourse',
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name='studentcourse',
            name='course',
        ),
        migrations.RemoveField(
            model_name='studentcourse',
            name='student',
        ),
        migrations.DeleteModel(
            name='Assign',
        ),
        migrations.DeleteModel(
            name='AssignTime',
        ),
        migrations.DeleteModel(
            name='Attendance',
        ),
        migrations.DeleteModel(
            name='AttendanceClass',
        ),
        migrations.DeleteModel(
            name='AttendanceTotal',
        ),
        migrations.DeleteModel(
            name='Marks',
        ),
        migrations.DeleteModel(
            name='MarksClass',
        ),
        migrations.DeleteModel(
            name='Student',
        ),
        migrations.DeleteModel(
            name='StudentCourse',
        ),
    ]
