# Generated by Django 4.1 on 2022-11-27 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="StudentData",
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
                ("studentName", models.CharField(max_length=60)),
                ("studentEmail", models.EmailField(max_length=60)),
                ("studentDob", models.DateField()),
                ("studentGender", models.CharField(max_length=7)),
                ("studentAddress1", models.CharField(max_length=100)),
                ("studentAddress2", models.CharField(max_length=100)),
                ("studentCity", models.CharField(max_length=25)),
                ("studentState", models.CharField(max_length=25)),
                ("studentCountry", models.CharField(default="", max_length=25)),
                ("studentPincode", models.CharField(max_length=10)),
                ("studentPhno", models.CharField(max_length=15)),
                ("studentQualification", models.CharField(max_length=25)),
                ("studentTQualification", models.CharField(max_length=25)),
                ("studentIdProof", models.CharField(max_length=25)),
                ("studentIdProofNo", models.CharField(max_length=25)),
                ("studentEnrolledin", models.CharField(max_length=25)),
                ("studentDoj", models.CharField(max_length=25)),
                ("studentEnrollNo", models.CharField(max_length=20)),
                ("studentCourseDuration", models.CharField(max_length=15)),
                ("studentFees", models.CharField(max_length=10)),
                ("studentDiscount", models.CharField(max_length=10)),
                ("studentRemark", models.CharField(max_length=50)),
                ("status", models.CharField(max_length=8)),
                ("addedBy", models.CharField(default="", max_length=25)),
            ],
            options={"verbose_name_plural": "Students",},
        ),
    ]
