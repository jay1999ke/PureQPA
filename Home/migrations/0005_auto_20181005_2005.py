# Generated by Django 2.1 on 2018-10-05 14:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0004_faculty'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='pureperson_ptr',
        ),
        migrations.DeleteModel(
            name='student',
        ),
    ]