# Generated by Django 4.1.5 on 2023-03-06 00:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tittle', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('products', models.ManyToManyField(blank=True, to='products.product')),
            ],
        ),
    ]
