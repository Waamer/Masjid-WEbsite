# Generated by Django 4.1.7 on 2023-06-16 01:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_personaldata_is_converted_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]