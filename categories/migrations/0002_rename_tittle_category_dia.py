# Generated by Django 4.1.7 on 2023-03-06 19:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='tittle',
            new_name='dia',
        ),
    ]
