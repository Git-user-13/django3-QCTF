# Generated by Django 4.2.1 on 2023-06-09 06:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0008_rename_leaderboard_board'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Myre',
            new_name='Flag',
        ),
    ]