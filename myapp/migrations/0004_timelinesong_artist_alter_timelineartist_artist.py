# Generated by Django 4.2.7 on 2023-12-07 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_timelineartist_timelinesong'),
    ]

    operations = [
        migrations.AddField(
            model_name='timelinesong',
            name='artist',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='timelineartist',
            name='artist',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
