# Generated by Django 2.1.5 on 2019-02-27 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Course', '0011_auto_20190227_1029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questionpaper',
            name='questions',
            field=models.ManyToManyField(related_name='question_of_course', to='Course.question'),
        ),
    ]
