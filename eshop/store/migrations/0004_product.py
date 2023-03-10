# Generated by Django 3.2.16 on 2023-03-01 15:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_alter_category_parent_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('code', models.CharField(max_length=150)),
                ('price', models.IntegerField()),
                ('discount_price', models.IntegerField(blank=True, null=True)),
                ('available_stock', models.IntegerField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.category')),
            ],
            options={
                'verbose_name_plural': 'Products',
            },
        ),
    ]
