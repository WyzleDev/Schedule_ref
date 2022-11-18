# Generated by Django 4.1 on 2022-09-14 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("schedule", "0003_alter_day_week"),
    ]

    operations = [
        migrations.AlterField(
            model_name="lesson",
            name="position",
            field=models.CharField(
                choices=[("1", "1"), ("2", "2"), ("3", "3"), ("4", "4"), ("5", "5")],
                default=("1", "1"),
                max_length=32,
                verbose_name="Номер пары",
            ),
        ),
    ]