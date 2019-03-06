# Generated by Django 2.1.5 on 2019-03-03 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Course', '0015_auto_20190303_1504'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='type',
            field=models.CharField(choices=[('binary', 'binary'), ('blank', 'blank'), ('wh', 'wh')], default='binary', max_length=20),
        ),
        migrations.AlterField(
            model_name='questionpaper',
            name='questions',
            field=models.ManyToManyField(related_name='question_of_course', to='Course.question'),
        ),
    ]