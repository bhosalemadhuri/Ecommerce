# Generated by Django 3.2.4 on 2021-06-16 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminmodule', '0010_chatmessages'),
    ]

    operations = [
        migrations.RenameField(
            model_name='chatmessages',
            old_name='recipient',
            new_name='receiver',
        ),
        migrations.AddField(
            model_name='chatmessages',
            name='sender',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
    ]
