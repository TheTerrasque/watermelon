# Generated by Django 2.0.7 on 2018-07-27 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Stream',
            fields=[
                ('url', models.URLField(primary_key=True, serialize=False)),
                ('format', models.CharField(blank=True, max_length=100)),
                ('bitrate', models.PositiveSmallIntegerField(default=0)),
                ('country_code', models.CharField(blank=True, max_length=2)),
                ('owner', models.CharField(blank=True, max_length=100)),
                ('notes', models.CharField(blank=True, max_length=200)),
            ],
        ),
    ]
