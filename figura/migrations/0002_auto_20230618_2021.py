# Generated by Django 4.1.2 on 2023-06-19 00:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('figura', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='figuras',
            name='id_figura'
        )
    ]
