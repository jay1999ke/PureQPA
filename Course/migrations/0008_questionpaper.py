# Generated by Django 2.1.5 on 2019-02-07 05:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Course', '0007_auto_20190207_1031'),
    ]

    operations = [
        migrations.CreateModel(
            name='questionPaper',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('examName', models.CharField(max_length=1024)),
                ('course', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='course_question_paper', to='Course.course')),
                ('questions', models.ManyToManyField(related_name='question_of_course', to='Course.question')),
            ],
        ),
    ]
