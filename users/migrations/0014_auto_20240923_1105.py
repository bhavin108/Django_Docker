# Generated by Django 3.1.8 on 2024-09-23 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0013_auto_20240922_2124'),
    ]

    operations = [
        migrations.AddField(
            model_name='present',
            name='username',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='time',
            name='username',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]
