# Generated by Django 2.1 on 2018-10-16 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Course', '0003_course_coursecode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='courseCode',
            field=models.CharField(max_length=8),
        ),
        migrations.AlterField(
            model_name='course',
            name='link',
            field=models.CharField(max_length=512),
        ),
    ]
