# Generated by Django 4.0.4 on 2022-08-31 12:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wndrland_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='subscriber_newsletter',
            table='tbl_temp_users',
        ),
    ]
