# Generated by Django 2.0.7 on 2018-07-27 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=200)),
                ('real_name', models.CharField(max_length=200)),
                ('country_code', models.CharField(blank=True, max_length=2)),
                ('bio', models.TextField(blank=True)),
            ],
        ),
    ]
