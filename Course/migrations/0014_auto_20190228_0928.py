# Generated by Django 2.1.5 on 2019-02-28 03:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Course', '0013_auto_20190228_0927'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questionpaper',
            name='questions',
            field=models.ManyToManyField(related_name='question_of_course', to='Course.question'),
        ),
    ]
