# Generated by Django 3.0.5 on 2021-04-22 23:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dmdbBaseManagement', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='father',
            field=models.CharField(default=None, max_length=50),
        ),
        migrations.AddField(
            model_name='student',
            name='mother',
            field=models.CharField(default=None, max_length=50),
        ),
    ]