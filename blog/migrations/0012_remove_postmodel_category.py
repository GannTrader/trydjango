# Generated by Django 3.1.1 on 2020-10-01 13:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_postmodel_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='postmodel',
            name='category',
        ),
    ]
