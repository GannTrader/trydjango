# Generated by Django 3.1.1 on 2020-10-01 06:16

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0004_postmodel_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='postmodel',
            name='likes',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
