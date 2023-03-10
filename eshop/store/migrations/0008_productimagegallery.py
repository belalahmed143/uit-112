# Generated by Django 3.2.16 on 2023-03-01 16:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_auto_20230301_2120'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductImageGallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('another_image', models.ImageField(upload_to='productImageGallery')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.product')),
            ],
            options={
                'verbose_name_plural': 'ProductImageGallerys',
            },
        ),
    ]
