# Generated by Django 2.1.5 on 2019-02-07 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Course', '0005_question'),
    ]

    operations = [
        migrations.CreateModel(
            name='questionPaper',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('questions', models.ManyToManyField(related_name='question_of_course', to='Course.question')),
            ],
        ),
    ]