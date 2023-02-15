# Generated by Django 3.2.16 on 2023-02-08 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uit_app', '0002_auto_20230208_2125'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('phone', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
            ],
        ),
    ]