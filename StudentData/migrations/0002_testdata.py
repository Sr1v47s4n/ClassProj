# Generated by Django 4.1 on 2022-11-28 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("StudentData", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="TestData",
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
                ("testing", models.CharField(max_length=200)),
            ],
        ),
    ]
