# Generated by Django 3.2.4 on 2021-06-18 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminmodule', '0014_negotiationdetails_negotiated_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chatmessages',
            name='message_date',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='orderdetails',
            name='ordered_date',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='paymentdetails',
            name='payment_date',
            field=models.DateField(auto_now_add=True),
        ),
    ]