# Generated by Django 5.0.3 on 2024-03-29 00:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='term',
            field=models.IntegerField(default=1, max_length=2),
        ),
    ]