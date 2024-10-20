# Generated by Django 5.1.2 on 2024-10-20 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_webdesignblocks_delete_webdesineblocks_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CampaignsBlock1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
                ('image_title', models.CharField(blank=True, max_length=255, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='campaigns.image.url')),
            ],
            options={
                'verbose_name': 'Campaigns blocks',
                'verbose_name_plural': 'Campaigns blocks',
            },
        ),
        migrations.CreateModel(
            name='CampaignsBlock2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
                ('image_title', models.CharField(blank=True, max_length=255, null=True)),
                ('video', models.FileField(blank=True, null=True, upload_to='media/videos/')),
            ],
            options={
                'verbose_name': 'Campaigns block2',
                'verbose_name_plural': 'Campaigns block2',
            },
        ),
        migrations.CreateModel(
            name='GraphicDesignBlock1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
                ('image_title', models.CharField(blank=True, max_length=255, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='graphic_design.image.url')),
            ],
            options={
                'verbose_name': 'Graphic Design block1',
                'verbose_name_plural': 'Graphic Design block1',
            },
        ),
        migrations.CreateModel(
            name='GraphicDesignBlock2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
                ('image_title', models.CharField(blank=True, max_length=255, null=True)),
                ('video', models.FileField(blank=True, null=True, upload_to='media/videos/')),
            ],
            options={
                'verbose_name': 'Graphic Design block2',
                'verbose_name_plural': 'Graphic Design block2',
            },
        ),
        migrations.CreateModel(
            name='WebDesignBlock1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
                ('image_title', models.CharField(blank=True, max_length=255, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='web_design.image.url')),
            ],
            options={
                'verbose_name': 'Web Design block1',
                'verbose_name_plural': 'Web Design block1',
            },
        ),
        migrations.CreateModel(
            name='WebDesignBlock2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
                ('image_title', models.CharField(blank=True, max_length=255, null=True)),
                ('video', models.FileField(blank=True, null=True, upload_to='media/videos/')),
            ],
            options={
                'verbose_name': 'Web Design block2',
                'verbose_name_plural': 'Web Design block2',
            },
        ),
        migrations.DeleteModel(
            name='CampaignsBlocks',
        ),
        migrations.DeleteModel(
            name='GraphicDesignBlocks',
        ),
        migrations.DeleteModel(
            name='WebDesignBlocks',
        ),
    ]
