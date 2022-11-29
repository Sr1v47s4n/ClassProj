# Generated by Django 4.1 on 2022-11-27 13:27

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="StaffData",
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
                ("password", models.CharField(max_length=128, verbose_name="password")),
                ("userName", models.CharField(max_length=220, unique=True)),
                ("staffName", models.CharField(default="User", max_length=50)),
                ("staffDob", models.DateField()),
                ("staffEmail", models.CharField(default="", max_length=50)),
                ("staffAddress1", models.CharField(default="", max_length=50)),
                ("staffAddress2", models.CharField(default="", max_length=50)),
                ("staffCity", models.CharField(default="", max_length=50)),
                ("staffState", models.CharField(default="", max_length=50)),
                ("staffCountry", models.CharField(default="", max_length=50)),
                ("staffPincode", models.CharField(default="", max_length=10)),
                ("staffPhNo", models.CharField(default="", max_length=50)),
                ("staffQualification", models.CharField(default="", max_length=50)),
                ("staffExperience", models.CharField(default="", max_length=50)),
                ("PreviousJob", models.CharField(default="", max_length=50)),
                ("staffDoj", models.DateField()),
                ("staffSubject", models.CharField(default="", max_length=50)),
                ("staffCourse", models.CharField(default="None", max_length=50)),
                ("staffHash", models.CharField(max_length=250)),
                ("addedBy", models.CharField(default="", max_length=25, null=True)),
                (
                    "UserRule",
                    models.CharField(
                        choices=[("1", "Admin"), ("2", "Staff")],
                        default="",
                        max_length=10,
                    ),
                ),
                ("is_staff", models.BooleanField(default=False)),
                ("is_active", models.BooleanField(default=True)),
                (
                    "date_joined",
                    models.DateTimeField(default=django.utils.timezone.now),
                ),
                ("last_login", models.DateTimeField(null=True)),
            ],
            options={"verbose_name_plural": "Staffs",},
        ),
    ]