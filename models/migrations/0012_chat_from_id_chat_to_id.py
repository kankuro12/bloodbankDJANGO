# Generated by Django 4.1.5 on 2023-01-24 01:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0011_chat'),
    ]

    operations = [
        migrations.AddField(
            model_name='chat',
            name='from_id',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='chat',
            name='to_id',
            field=models.IntegerField(null=True),
        ),
    ]