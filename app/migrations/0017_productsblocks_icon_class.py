# Generated by Django 5.1.2 on 2024-10-21 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0016_products_productsblocks'),
    ]

    operations = [
        migrations.AddField(
            model_name='productsblocks',
            name='icon_class',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]