# Generated by Django 5.1.2 on 2024-10-14 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Featured_Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='featured_products')),
                ('product_name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Featured Products',
            },
        ),
    ]
