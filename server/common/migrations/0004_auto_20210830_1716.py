# Generated by Django 3.2.6 on 2021-08-30 08:16

import common.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0003_alter_usercustomizableinfo_profile_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='usercustomizableinfo',
            name='img_height',
            field=models.PositiveIntegerField(blank=True, default=200),
        ),
        migrations.AddField(
            model_name='usercustomizableinfo',
            name='img_width',
            field=models.PositiveIntegerField(blank=True, default=200),
        ),
        migrations.AlterField(
            model_name='usercustomizableinfo',
            name='profile_img',
            field=models.ImageField(blank=True, height_field=models.PositiveIntegerField(blank=True, default=200), null=True, upload_to=common.models.user_directory_path, width_field=models.PositiveIntegerField(blank=True, default=200)),
        ),
    ]
