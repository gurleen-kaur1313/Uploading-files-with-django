# Generated by Django 3.1.6 on 2021-02-08 00:46

from django.db import migrations, models
import files.models


class Migration(migrations.Migration):

    dependencies = [
        ('files', '0005_auto_20210208_0613'),
    ]

    operations = [
        migrations.AlterField(
            model_name='files',
            name='file',
            field=models.ImageField(blank=True, null=True, upload_to=files.models.userimage_profile_file_path),
        ),
    ]
