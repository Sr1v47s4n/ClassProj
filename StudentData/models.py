from django.db import models


class StudentData(models.Model):
    studentName = models.CharField(max_length=60, null=False)
    studentEmail = models.EmailField(max_length=60, null=False)
    studentDob = models.DateField()
    studentGender = models.CharField(max_length=7, null=False)
    studentAddress1 = models.CharField(max_length=100, null=False)
    studentAddress2 = models.CharField(max_length=100, null=False)
    studentCity = models.CharField(max_length=25, null=False)
    studentState = models.CharField(max_length=25, null=False)
    studentCountry = models.CharField(max_length=25, null=False, default="")
    studentPincode = models.CharField(max_length=10, null=False)
    studentPhno = models.CharField(max_length=15, null=False)
    studentQualification = models.CharField(max_length=25, null=False)
    studentTQualification = models.CharField(max_length=25, null=False)
    studentIdProof = models.CharField(max_length=25, null=False)
    studentIdProofNo = models.CharField(max_length=25, null=False)
    studentEnrolledin = models.CharField(max_length=25, null=False)
    studentDoj = models.CharField(max_length=25, null=False)
    studentEnrollNo = models.CharField(max_length=20, null=False)
    studentCourseDuration = models.CharField(max_length=15, null=False)
    studentFees = models.CharField(max_length=10, null=False)
    studentDiscount = models.CharField(max_length=10, null=False)
    studentRemark = models.CharField(max_length=50, null=False)
    status = models.CharField(max_length=8, null=False)
    addedBy = models.CharField(max_length=25, null=False, default="")

    def __str__(self):
        return self.studentName

    class Meta:
        verbose_name_plural = "Students"

class TestData(models.Model):
    testing = models.CharField(max_length=200)