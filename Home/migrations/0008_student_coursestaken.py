# Generated by Django 2.1 on 2018-10-17 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Course', '0004_auto_20181016_1859'),
        ('Home', '0007_pureperson_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='coursesTaken',
            field=models.ManyToManyField(related_name='course_instudents', to='Course.course'),
        ),
    ]
