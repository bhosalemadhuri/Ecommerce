# Generated by Django 3.2.4 on 2021-06-26 09:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adminmodule', '0024_advertisement'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='advertisement',
            name='description',
        ),
        migrations.RemoveField(
            model_name='advertisement',
            name='product_name',
        ),
    ]
