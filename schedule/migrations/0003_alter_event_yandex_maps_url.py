# Generated by Django 4.1 on 2022-08-31 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0002_alter_group_options_event_yandex_maps_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='yandex_maps_url',
            field=models.URLField(blank=True, null=True, verbose_name='Ссылка на яндекс карты'),
        ),
    ]
