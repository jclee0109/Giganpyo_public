# Generated by Django 3.1.3 on 2021-07-23 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timetable', '0003_evaluation_subjecteval'),
    ]

    operations = [
        migrations.AddField(
            model_name='subjectinfo',
            name='select_person',
            field=models.PositiveSmallIntegerField(blank=True, default=0, null=True),
        ),
    ]
