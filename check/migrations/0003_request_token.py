# Generated by Django 3.1.12 on 2021-07-08 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('check', '0002_request_approved'),
    ]

    operations = [
        migrations.AddField(
            model_name='request',
            name='token',
            field=models.CharField(default='', max_length=150),
            preserve_default=False,
        ),
    ]
