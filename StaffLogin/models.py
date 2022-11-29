from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models
from django.utils import timezone


class StaffData(AbstractBaseUser):
    userName = models.CharField(max_length=220, null=False, blank=False, unique=True)
    staffName = models.CharField(max_length=50, null=False, default="User")
    staffDob = models.DateField()
    staffEmail = models.CharField(max_length=50, null=False, default="")
    staffAddress1 = models.CharField(max_length=50, null=False, default="")
    staffAddress2 = models.CharField(max_length=50, null=False, default="")
    staffCity = models.CharField(max_length=50, null=False, default="")
    staffState = models.CharField(max_length=50, null=False, default="")
    staffCountry = models.CharField(max_length=50, null=False, default="")
    staffPincode = models.CharField(max_length=10, null=False, default="")
    staffPhNo = models.CharField(max_length=50, null=False, default="")
    staffQualification = models.CharField(max_length=50, null=False, default="")
    staffExperience = models.CharField(max_length=50, null=False, default="")
    PreviousJob = models.CharField(max_length=50, null=False, default="")
    staffDoj = models.DateField()
    staffSubject = models.CharField(max_length=50, null=False, default="")
    staffCourse = models.CharField(max_length=50, null=False, default="None")
    staffHash = models.CharField(max_length=250, null=True, default="None")
    addedBy = models.CharField(max_length=25, null=True, default="")
    rule = (("1", "Admin"), ("2", "Staff"))
    UserRule = models.CharField(max_length=10, null=False, choices=rule, default="")
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    last_login = models.DateTimeField(null=True)
    objects = BaseUserManager()
    USERNAME_FIELD = "userName"
    REQUIRED_FIELDS = [
        "staffName",
        "staffEmail",
        "staffDob",
        "staffPhNo",
        "staffAddress1",
        "staffAddress2",
        "staffCity",
        "staffState",
        "staffCountry",
        "staffPincode",
        "staffQualification",
        "staffExperience",
        "staffCourse",
        "staffSubject",
        "staffHash",
        "staffDoj",
        "PreviousJob",
        "addedBy",
    ]

    def __str__(self):
        return f"{self.staffName}"

    class Meta:
        verbose_name_plural = "Staffs"
