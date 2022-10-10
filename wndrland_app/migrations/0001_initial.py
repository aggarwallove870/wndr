# Generated by Django 4.0.4 on 2022-10-07 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='contact_us',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('review', models.CharField(max_length=500)),
            ],
            options={
                'verbose_name': 'Contact u',
            },
        ),
        migrations.CreateModel(
            name='DesktopMobileVideo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desktop_top_video', models.CharField(max_length=200)),
                ('mobile_top_video', models.CharField(max_length=200)),
                ('desktop_bottom_video', models.CharField(max_length=300)),
                ('mobile_bottom_video', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Subscriber_newsletter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Subscriber',
            },
        ),
    ]
