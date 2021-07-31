# Generated by Django 3.2.4 on 2021-06-25 13:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('adminmodule', '0023_alter_product_product_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='advertisement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('product_image', models.ImageField(upload_to='pics')),
                ('product_number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminmodule.product')),
            ],
        ),
    ]