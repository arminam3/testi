# Generated by Django 5.0.3 on 2024-04-09 01:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_verificationcode'),
    ]

    operations = [
        migrations.RenameField(
            model_name='verificationcode',
            old_name='created_at',
            new_name='datetime_created',
        ),
    ]