# Generated by Django 4.0.4 on 2022-09-14 05:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wndrland_app', '0006_rename_videourl_video_video_desktop_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='video_desktop_url',
            field=models.FileField(null=True, upload_to='videos', verbose_name=''),
        ),
    ]
