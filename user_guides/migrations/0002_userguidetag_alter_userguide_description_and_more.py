# Generated by Django 4.1 on 2022-10-12 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user_guides", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="UserGuideTag",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255, unique=True)),
            ],
            options={
                "verbose_name": "Тег",
                "verbose_name_plural": "Теги",
            },
        ),
        migrations.AlterField(
            model_name="userguide",
            name="description",
            field=models.TextField(verbose_name="Описание"),
        ),
        migrations.AddField(
            model_name="userguide",
            name="tags",
            field=models.ManyToManyField(
                to="user_guides.userguidetag", verbose_name="Теги"
            ),
        ),
    ]