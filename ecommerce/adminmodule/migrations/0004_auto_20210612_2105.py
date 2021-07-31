# Generated by Django 3.2.4 on 2021-06-12 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminmodule', '0003_cart_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdetails',
            name='address',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='userdetails',
            name='city',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='userdetails',
            name='country',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='userdetails',
            name='phonenumber',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='userdetails',
            name='pincode',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='userdetails',
            name='state',
            field=models.CharField(max_length=100, null=True),
        ),
    ]