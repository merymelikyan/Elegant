# Generated by Django 5.1.2 on 2024-10-19 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='headertext',
            name='description',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
