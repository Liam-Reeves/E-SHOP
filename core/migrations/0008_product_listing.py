# Generated by Django 5.1 on 2024-11-02 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_slider'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product_Listing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='product_listing')),
                ('name_of_product', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
            options={
                'verbose_name_plural': 'Product Listings',
            },
        ),
    ]