# Generated by Django 2.1.5 on 2019-02-27 04:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Course', '0011_auto_20190227_1029'),
        ('Home', '0014_remove_faculty_salary'),
    ]

    operations = [
        migrations.AddField(
            model_name='faculty',
            name='courses',
            field=models.ManyToManyField(blank=True, related_name='course_faculties', to='Course.course'),
        ),
    ]
