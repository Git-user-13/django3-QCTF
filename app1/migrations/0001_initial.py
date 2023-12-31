# Generated by Django 4.2.1 on 2023-06-02 09:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('created_at', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('hint_1', models.CharField(blank=True, max_length=200)),
                ('flag_1', models.CharField(blank=True, max_length=200)),
                ('hint_2', models.CharField(blank=True, max_length=200)),
                ('flag_2', models.CharField(blank=True, max_length=200)),
                ('hint_3', models.CharField(blank=True, max_length=200)),
                ('flag_3', models.CharField(blank=True, max_length=200)),
                ('hint_4', models.CharField(blank=True, max_length=200)),
                ('flag_4', models.CharField(blank=True, max_length=200)),
                ('hint_5', models.CharField(blank=True, max_length=200)),
                ('flag_5', models.CharField(blank=True, max_length=200)),
            ],
        ),
    ]
