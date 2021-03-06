# Generated by Django 3.2.4 on 2021-06-17 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminmodule', '0011_auto_20210616_2025'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderdetails',
            old_name='status',
            new_name='negotiation_status',
        ),
        migrations.AddField(
            model_name='cart',
            name='discount_price',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cart',
            name='negotiation_status',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='orderdetails',
            name='discount_price',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='orderdetails',
            name='order_status',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
    ]
