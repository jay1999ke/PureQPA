# Generated by Django 2.1.5 on 2019-04-23 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Course', '0038_auto_20190423_2055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questionpaper',
            name='questions',
            field=models.ManyToManyField(related_name='questions_of_paper', to='Course.question'),
        ),
    ]