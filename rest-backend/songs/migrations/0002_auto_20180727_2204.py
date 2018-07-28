# Generated by Django 2.0.7 on 2018-07-27 20:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('songs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SongStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='platform',
            name='id',
            field=models.AutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='song',
            name='added',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='song',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='song',
            name='uploaded_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='songs', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='platform',
            name='name',
            field=models.CharField(max_length=200),
        ),
        migrations.AddField(
            model_name='song',
            name='status',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='songs.SongStatus'),
            preserve_default=False,
        ),
    ]