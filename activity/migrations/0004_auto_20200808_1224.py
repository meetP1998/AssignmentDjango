# Generated by Django 3.0.7 on 2020-08-08 06:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('activity', '0003_auto_20200808_1220'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='Users',
        ),
    ]