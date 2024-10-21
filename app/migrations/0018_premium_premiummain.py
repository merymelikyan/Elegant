# Generated by Django 5.1.2 on 2024-10-21 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0017_productsblocks_icon_class'),
    ]

    operations = [
        migrations.CreateModel(
            name='Premium',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='premium')),
            ],
            options={
                'verbose_name': 'Premium',
                'verbose_name_plural': 'Premium',
            },
        ),
        migrations.CreateModel(
            name='PremiumMain',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Premium Main',
                'verbose_name_plural': 'Premium Main',
            },
        ),
    ]
