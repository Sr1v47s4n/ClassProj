from .models import StudentData
from django.forms import ModelForm


class AddStudent(ModelForm):
    class Meta:
        model = StudentData
        fields = ["studentName",
            "studentEmail",
            "studentDob",
            "studentGender",
            "studentAddress1",
            "studentAddress2",
            "studentCity",
            "studentState",
            "studentCountry",
            "studentPincode",
            "studentPhno",
            "studentQualification",
            "studentTQualification",
            "studentIdProof",
            "studentIdProofNo",
            "studentEnrolledin",
            "studentDoj",
            "studentEnrollNo",
            "studentCourseDuration",
            "studentFees",
            "studentDiscount",
            "studentRemark",
            "status",
            "addedBy"]
        
