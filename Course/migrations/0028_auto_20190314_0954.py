# Generated by Django 2.1.5 on 2019-03-14 04:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Course', '0027_auto_20190311_0939'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questionpaper',
            name='questions',
            field=models.ManyToManyField(related_name='question_of_course', to='Course.question'),
        ),
    ]