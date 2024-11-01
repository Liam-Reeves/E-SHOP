# Generated by Django 5.1.2 on 2024-10-25 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_delete_slider'),
    ]

    operations = [
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='slider')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, max_length=250)),
            ],
            options={
                'verbose_name_plural': 'Slider',
            },
        ),
    ]
