# Generated by Django 3.0.4 on 2020-03-28 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fullthrottle_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='tz',
            field=models.CharField(choices=[('America/Los_Angeles', 'America/Los_Angeles'), ('Asia/Kolkata', 'Asia/Kolkata')], max_length=100),
        ),
    ]
