# Generated by Django 4.1.5 on 2023-01-08 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0004_bloodrequest_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='bloodrequest',
            name='completed',
            field=models.BooleanField(default=False),
        ),
    ]