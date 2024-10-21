# Generated by Django 5.1.2 on 2024-10-21 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_alter_contactphone_phone_number1_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='OpeningHours',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60)),
                ('days1', models.CharField(max_length=60)),
                ('days2', models.CharField(max_length=60)),
                ('days3', models.CharField(max_length=60)),
                ('days4', models.CharField(max_length=60)),
                ('days5', models.CharField(max_length=60)),
                ('days6', models.CharField(max_length=60)),
                ('open_time1', models.CharField(max_length=60)),
                ('open_time2', models.CharField(max_length=60)),
                ('open_time3', models.CharField(max_length=60)),
                ('open_time4', models.CharField(max_length=60)),
                ('open_time5', models.CharField(max_length=60)),
                ('open_time6', models.CharField(max_length=60)),
                ('close_day', models.CharField(max_length=60)),
                ('close_time', models.CharField(max_length=60)),
            ],
            options={
                'verbose_name': 'Opening Hours',
                'verbose_name_plural': 'Opening Hours',
            },
        ),
        migrations.AlterField(
            model_name='galleryblocks',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='block.image.url'),
        ),
    ]