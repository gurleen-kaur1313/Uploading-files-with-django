# Generated by Django 3.1.6 on 2021-02-08 00:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('files', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='files',
            name='created',
            field=models.DateField(auto_created=True, blank=True, null=True),
        ),
    ]