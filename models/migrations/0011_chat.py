# Generated by Django 4.1.5 on 2023-01-24 01:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0010_bloodrequest_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('ident', models.CharField(max_length=50)),
                ('senderName', models.CharField(max_length=50)),
                ('receiverName', models.CharField(max_length=50)),
                ('message', models.TextField()),
            ],
        ),
    ]
