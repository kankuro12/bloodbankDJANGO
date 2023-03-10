# Generated by Django 4.1.5 on 2023-01-08 17:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0002_location'),
    ]

    operations = [
        migrations.CreateModel(
            name='BloodRequest',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('blood_group', models.CharField(max_length=3)),
                ('amount', models.IntegerField()),
                ('date', models.DateField()),
                ('hospital', models.CharField(max_length=50)),
                ('address', models.TextField()),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='models.location')),
            ],
        ),
    ]
