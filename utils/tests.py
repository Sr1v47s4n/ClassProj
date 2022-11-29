from django.test import TestCase
from StaffLogin.models import StaffData
from StudentData.models import StudentData

# Create your tests here.


class staffdataTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.staff = StaffData.objects.create(
            userName="user1",
            staffName="MyStaff",
            staffDob="2001-09-03",
            staffEmail="email@g.co",
            staffAddress1="add1",
            staffAddress2="add2",
            staffCity="City",
            staffState="state",
            staffCountry="coun",
            staffPincode="pin",
            staffPhNo="no",
            staffQualification="qu",
            staffExperience="1",
            PreviousJob="N",
            staffDoj="2001-02-01",
            staffSubject="cs",
            staffCourse="py",
            addedBy="admin",
            UserRule="1",
        )

    def test_data(self):
        self.assertEqual(self.staff.staffName, "MyStaff")
        self.assertEqual(self.staff.staffDob, "2001-09-03")
        self.assertEqual(self.staff.staffEmail, "email@g.co")


class studentdataTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.stu = StudentData.objects.create(
            studentName="Test",
            studentEmail="email@k.vb",
            studentDob="2001-02-25",
            studentGender="M",
            studentAddress1="Addd1",
            studentAddress2="Addd2",
            studentCity="City",
            studentState="State",
            studentCountry="IN",
            studentPincode="250",
            studentPhno="254125",
            studentQualification="vjg",
            studentTQualification="Tq",
            studentIdProof="ID",
            studentIdProofNo="15",
            studentEnrolledin="Python",
            studentDoj="2005-02-25",
            studentEnrollNo="2541",
            studentCourseDuration="ds",
            studentFees="365",
            studentDiscount="12%",
            studentRemark="No",
            status="active",
            addedBy="Testing",
        )

    def test_data(self):
        self.assertEqual(self.stu.studentName, "Test")
        self.assertEqual(self.stu.studentDoj, "2005-02-25")
        self.assertEqual(self.stu.studentEnrolledin, "Python")
