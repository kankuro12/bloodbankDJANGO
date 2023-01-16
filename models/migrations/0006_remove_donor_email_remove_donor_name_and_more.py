# Generated by Django 4.1.5 on 2023-01-09 01:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('models', '0005_bloodrequest_completed'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='donor',
            name='email',
        ),
        migrations.RemoveField(
            model_name='donor',
            name='name',
        ),
        migrations.AddField(
            model_name='bloodrequest',
            name='lan',
            field=models.DecimalField(decimal_places=8, default=84.124, max_digits=12),
        ),
        migrations.AddField(
            model_name='bloodrequest',
            name='lat',
            field=models.DecimalField(decimal_places=8, default=28.3949, max_digits=12),
        ),
        migrations.AddField(
            model_name='donor',
            name='blood_group',
            field=models.CharField(max_length=3, null=True),
        ),
        migrations.AddField(
            model_name='donor',
            name='lan',
            field=models.DecimalField(decimal_places=8, default=84.124, max_digits=12),
        ),
        migrations.AddField(
            model_name='donor',
            name='lat',
            field=models.DecimalField(decimal_places=8, default=28.3949, max_digits=12),
        ),
        migrations.AddField(
            model_name='donor',
            name='location',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='models.location'),
        ),
        migrations.AddField(
            model_name='donor',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]