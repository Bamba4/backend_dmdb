# Generated by Django 3.0.5 on 2021-04-26 15:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dmdbBaseManagement', '0005_auto_20210426_0713'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='is_memorize_quran',
            new_name='has_memorized',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='is_recite_all_quran',
            new_name='has_recited',
        ),
    ]