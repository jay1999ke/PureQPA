# Generated by Django 2.1.5 on 2019-04-01 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Course', '0031_auto_20190317_1534'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='answer',
            field=models.CharField(default=True, max_length=1024),
        ),
        migrations.AlterField(
            model_name='questionpaper',
            name='questions',
            field=models.ManyToManyField(related_name='question_of_course', to='Course.question'),
        ),
    ]