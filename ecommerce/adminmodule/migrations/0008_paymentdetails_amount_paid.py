# Generated by Django 3.2.4 on 2021-06-13 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminmodule', '0007_paymentdetails'),
    ]

    operations = [
        migrations.AddField(
            model_name='paymentdetails',
            name='amount_paid',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
    ]
