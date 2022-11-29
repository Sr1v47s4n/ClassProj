from django.urls import reverse_lazy
from django.http import HttpResponse
from django.views import generic
from .models import StudentData
from django.contrib.auth.mixins import LoginRequiredMixin


class CreateTest(LoginRequiredMixin, generic.CreateView):
    login_url = "login/"
    model = StudentData
    fields = [
        "studentName",
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
        "addedBy",
    ]
    success_url = reverse_lazy("test")
    template_name = "cstudent.html"

    def form_invalid(self, form):
        error_message = "Error Try Again"
        return super().form_invalid(form)


# from django.http import HttpResponse
# from django.shortcuts import render, redirect
# from django.contrib.auth.hashers import make_password, check_password
# from .models import Student, Staff
# from django.contrib import messages
# from django.contrib.auth import logout, login
# from django.db.models import Q


# # Create your views here.


# def login_usr(request):
#     if request.method == "POST":
#         UserName = request.POST.get("UserName")
#         Password = request.POST.get("Password")
#         try:
#             user = Staff.objects.get(UserName=UserName)

#             if check_password(Password, user.Password) or Password == user.Password:
#                 print(user.UserRule)
#                 if user.UserRule != "null" and "2" == user.UserRule:
#                     # messages.success(request, "Logged as Staff")
#                     url = "staffPanel/{}".format(user.id)
#                     return redirect(url)
#                 elif "1" == user.UserRule:
#                     # messages.success(request, "Logged as Admin")
#                     return redirect("adminPanel", id=user.id)
#             else:
#                 messages.error(request, "Password Not Matched")
#                 return render(request, "login.html")

#         except Staff.DoesNotExist:
#             messages.error(request, "User Not Found")
#             return render(request, "login.html")

#     return render(request, "login.html")


# # Created By Srivatsan Sk
# def home(request):
#     return render(request, "home.html")


# def logout_usr(request):
#     messages.success(request, "Logged Out Successful")
#     l = logout(request)
#     print(l)
#     return redirect("login_usr")


class addStudent(LoginRequiredMixin, generic.CreateView):
    login_url = "login/"
    model = StudentData
    fields = [
        "studentName",
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
        "addedBy",
    ]
    success_url = "test"
    template_name = "cstudent.html"

    def form_invalid(self, form):
        error_message = "Error Try Again"
        return super().form_invalid(form)


# def addStudent(request, UserName):
#     if request.method == "POST":
#         studentName = request.POST.get("studentName")
#         studentEmail = request.POST.get("studentEmail")
#         studentDob = request.POST.get("studentDob")
#         studentGender = request.POST.get("studentGender")
#         studentAddress1 = request.POST.get("studentAddress1")
#         studentAddress2 = request.POST.get("studentAddress2")
#         studentCity = request.POST.get("studentCity")
#         studentState = request.POST.get("studentState")
#         studentCountry = request.POST.get("studentCountry")
#         studentPincode = request.POST.get("studentPincode")
#         studentPhno = request.POST.get("studentPhno")
#         addedBy = UserName
#         studentQualification = request.POST.get("studentQualification")
#         studentTQualification = request.POST.get("studentTQualification")
#         studentIdProof = request.POST.get("studentIdProof")
#         studentIdProofNo = request.POST.get("studentIdProofNo")
#         studentEnrolledin = request.POST.get("studentEnrolledin")
#         studentDoj = request.POST.get("studentDoj")
#         studentEnrollNo = request.POST.get("studentEnrollNo")
#         studentCourseDuration = request.POST.get("studentCourseDuration")
#         studentFees = request.POST.get("studentFees")
#         studentDiscount = request.POST.get("studentDiscount")
#         studentRemark = request.POST.get("studentRemark")
#         status = request.POST.get("status")

#         students = Student(
#             studentName=studentName,
#             studentEmail=studentEmail,
#             studentDob=studentDob,
#             studentGender=studentGender,
#             studentAddress1=studentAddress1,
#             studentAddress2=studentAddress2,
#             studentCity=studentCity,
#             studentState=studentState,
#             studentCountry=studentCountry,
#             studentPincode=studentPincode,
#             studentPhno=studentPhno,
#             studentQualification=studentQualification,
#             studentTQualification=studentTQualification,
#             studentIdProof=studentIdProof,
#             studentIdProofNo=studentIdProofNo,
#             studentEnrolledin=studentEnrolledin,
#             studentEnrollNo=studentEnrollNo,
#             studentDoj=studentDoj,
#             studentCourseDuration=studentCourseDuration,
#             studentFees=studentFees,
#             studentDiscount=studentDiscount,
#             studentRemark=studentRemark,
#             addedBy=addedBy,
#             status=status,
#         )
#         students.save()

#         return render(request, "manageStudent")

#     return render(request, "addStudent.html")


# def forgotpwd(request):
#     if request.method == "POST":
#         UserName = request.POST.get("UserName")
#         CurrentPassword = request.POST.get("CurrentPassword")
#         Password = request.POST.get("Password")
#         ConfirmPassword = request.POST.get("ConfirmPassword")

#         try:
#             user = Staff.objects.get(UserName=UserName)
#             if check_password(CurrentPassword, user.Password):
#                 if CurrentPassword == Password:
#                     messages.error(request, "Give New Password")
#                     return render(request, "forgotpwd.html")
#                 elif CurrentPassword != Password:
#                     if ConfirmPassword == Password:
#                         user.Password = make_password(user.clean_fields(Password))
#                         user.save(update_fields=["Password"])
#                         messages.success(request, "Password Changed Successful")
#                         return render(request, "login.html")
#                     else:
#                         messages.error(request, "Confirm Password Not Matched")
#                         return render(request, "forgotpwd.html")

#             else:
#                 messages.error(request, "Password Not Matched")
#                 return render(request, "forgotpwd.html")

#         except Staff.DoesNotExist:
#             messages.error(request, "User Not Found")
#             return render(request, "forgotpwd.html")

#     return render(request, "forgotpwd.html")


# def adminPanel(request, id):
#     staffs = Staff.objects.get(id=id)
#     return render(request, "adminPanel.html", {"staffs": staffs})


# def addStaff(request, CurrentUserName):
#     staffs = Staff.objects.get(UserName=CurrentUserName)

#     if request.method == "POST":
#         staffName = request.POST.get("staffName")
#         staffDob = request.POST.get("staffDob")
#         staffEmail = request.POST.get("staffEmail")
#         staffAddress1 = request.POST.get("staffAddress1")
#         staffAddress2 = request.POST.get("staffAddress2")
#         staffCity = request.POST.get("staffCity")
#         staffState = request.POST.get("staffState")
#         staffCountry = request.POST.get("staffCountry")
#         staffPincode = request.POST.get("staffPincode")
#         staffPhNo = request.POST.get("staffPhNo")
#         staffQualification = request.POST.get("staffQualification")
#         staffExperience = request.POST.get("staffExperience")
#         PreviousJob = request.POST.get("PreviousJob")
#         staffDoj = request.POST.get("staffDoj")
#         staffSubject = request.POST.get("staffSubject")
#         staffCourse = request.POST.get("staffCourse")
#         addedBy = staffs.UserName
#         UserName = request.POST.get("UserName")
#         Password = make_password(request.POST.get("Password"))
#         UserRule = request.POST.get("UserRule")
#         staffs = Staff(
#             staffName=staffName,
#             staffDob=staffDob,
#             staffEmail=staffEmail,
#             staffAddress1=staffAddress1,
#             staffAddress2=staffAddress2,
#             staffCity=staffCity,
#             staffState=staffState,
#             staffCountry=staffCountry,
#             staffPincode=staffPincode,
#             staffPhNo=staffPhNo,
#             staffQualification=staffQualification,
#             staffExperience=staffExperience,
#             PreviousJob=PreviousJob,
#             staffDoj=staffDoj,
#             staffSubject=staffSubject,
#             staffCourse=staffCourse,
#             UserName=UserName,
#             Password=Password,
#             UserRule=UserRule,
#             addedBy=addedBy,
#         )
#         staffs.clean_fields()
#         staffs.save()
#         return redirect("manageStaff")

#     return render(request, "addStaff.html",{'staffs':staffs})


# def manageStudent(request, UserName):
#     staffs = Staff.objects.get(UserName=UserName)
#     students = Student.objects.all()
#     return render(
#         request, "manageStudent.html", {"students": students, "staffs": staffs}
#     )


class manageStudent(LoginRequiredMixin, generic.ListView):
    model = StudentData
    template_name = "manageStudent.html"


# def staffmanageStudent(request, UserName):
#     staffs = Staff.objects.get(UserName=UserName)
#     students = Student.objects.all()
#     return render(
#         request, "staffmanageStudent.html", {"students": students, "staffs": staffs}
#     )


# def manageStaff(request, UserName):
#     currentStaffs = Staff.objects.get(UserName=UserName)
#     staffs = Staff.objects.all()
#     return render(
#         request, "manageStaff.html", {"staffs": staffs, "currentStaffs": currentStaffs}
#     )


# def editStaff(request, id):
#     staffs = Staff.objects.get(id=id)
#     return render(request, "editStaff.html", {"staffs": staffs})


# def editStaffData(request, id):

#     if request.method == "POST":
#         staffName = request.POST.get("staffName")
#         staffDob = request.POST.get("staffDob")
#         staffEmail = request.POST.get("staffEmail")
#         staffAddress1 = request.POST.get("staffAddress1")
#         staffAddress2 = request.POST.get("staffAddress2")
#         staffCity = request.POST.get("staffCity")
#         staffState = request.POST.get("staffState")
#         staffCountry = request.POST.get("staffCountry")
#         staffPincode = request.POST.get("staffPincode")
#         staffPhNo = request.POST.get("staffPhNo")
#         staffQualification = request.POST.get("staffQualification")
#         staffExperience = request.POST.get("staffExperience")
#         PreviousJob = request.POST.get("PreviousJob")
#         staffDoj = request.POST.get("staffDoj")
#         staffSubject = request.POST.get("staffSubject")
#         staffCourse = request.POST.get("staffCourse")
#         UserName = request.POST.get("UserName")
#         Password = make_password(request.POST.get("Password"))
#         UserRule = request.POST.get("UserRule")
#         addedBy = request.POST.get("addedBy")
#         staffs = Staff.objects.get(id=id)
#         staffs.staffName = staffName
#         staffs.staffDob = staffDob
#         staffs.staffEmail = staffEmail
#         staffs.staffAddress1 = staffAddress1
#         staffs.staffAddress2 = staffAddress2
#         staffs.staffCity = staffCity
#         staffs.staffState = staffState
#         staffs.staffCountry = staffCountry
#         staffs.staffPincode = staffPincode
#         staffs.staffPhNo = staffPhNo
#         staffs.staffQualification = staffQualification
#         staffs.staffExperience = staffExperience
#         staffs.PreviousJob = PreviousJob
#         staffs.staffDoj = staffDoj
#         staffs.staffSubject = staffSubject
#         staffs.staffCourse = staffCourse
#         staffs.UserName = UserName
#         staffs.Password = Password
#         staffs.UserRule = UserRule
#         staffs.addedBy = addedBy
#         staffs.save(
#             update_fields=[
#                 "staffName",
#                 "staffDob",
#                 "staffEmail",
#                 "staffAddress1",
#                 "staffAddress2",
#                 "staffCity",
#                 "staffState",
#                 "staffCountry",
#                 "staffPincode",
#                 "staffPhNo",
#                 "staffQualification",
#                 "staffExperience",
#                 "PreviousJob",
#                 "staffDoj",
#                 "staffSubject",
#                 "staffCourse",
#                 "UserName",
#                 "Password",
#                 "UserRule",
#             ]
#         )
#         return redirect("manageStaff")

#     return render(request, "manageStaff.html")


# def staffPanel(request, id):
#     staffs = Staff.objects.get(id=id)
#     return render(request, "staffPanel.html", {"staffs": staffs})


# def editStudent(request, id):
#     student = Student.objects.get(id=id)
#     return render(request, "editStudent.html", {"student": student})


# def editStudentData(request, id):

#     if request.method == "POST":
#         studentName = request.POST.get("studentName")
#         studentEmail = request.POST.get("studentEmail")
#         studentDob = request.POST.get("studentDob")
#         studentGender = request.POST.get("studentGender")
#         studentAddress1 = request.POST.get("studentAddress1")
#         studentAddress2 = request.POST.get("studentAddress2")
#         studentCity = request.POST.get("studentCity")
#         studentState = request.POST.get("studentState")
#         studentCountry = request.POST.get("studentCountry")
#         studentPincode = request.POST.get("studentPincode")
#         studentPhno = request.POST.get("studentPhno")
#         studentQualification = request.POST.get("studentQualification")
#         studentTQualification = request.POST.get("studentTQualification")
#         studentIdProof = request.POST.get("studentIdProof")
#         studentIdProofNo = request.POST.get("studentIdProofNo")
#         studentEnrolledin = request.POST.get("studentEnrolledin")
#         studentDoj = request.POST.get("studentDoj")
#         studentEnrollNo = request.POST.get("studentEnrollNo")
#         studentCourseDuration = request.POST.get("studentCourseDuration")
#         studentFees = request.POST.get("studentFees")
#         studentDiscount = request.POST.get("studentDiscount")
#         studentRemark = request.POST.get("studentRemark")
#         status = request.POST.get("status")
#         students = Student.objects.get(id=id)

#         students.studentName = studentName
#         students.studentEmail = studentEmail
#         students.studentDob = studentDob
#         students.studentGender = studentGender
#         students.studentAddress1 = studentAddress1
#         students.studentAddress2 = studentAddress2
#         students.studentCity = studentCity
#         students.studentState = studentState
#         students.studentCountry = studentCountry
#         students.studentPincode = studentPincode
#         students.studentPhno = studentPhno
#         students.studentQualification = studentQualification
#         students.studentTQualification = studentTQualification
#         students.studentIdProof = studentIdProof
#         students.studentIdProofNo = studentIdProofNo
#         students.studentEnrolledin = studentEnrolledin
#         students.studentEnrollNo = studentEnrollNo
#         students.studentDoj = studentDoj
#         students.studentCourseDuration = studentCourseDuration
#         students.studentFees = studentFees
#         students.studentDiscount = studentDiscount
#         students.studentRemark = studentRemark
#         students.status = status

#         students.save(
#             update_fields=[
#                 "studentName",
#                 "studentEmail",
#                 "studentDob",
#                 "studentGender",
#                 "studentAddress1",
#                 "studentAddress2",
#                 "studentCity",
#                 "studentState",
#                 "studentCountry",
#                 "studentPincode",
#                 "studentPhno",
#                 "studentQualification",
#                 "studentTQualification",
#                 "studentIdProof",
#                 "studentIdProofNo",
#                 "studentEnrolledin",
#                 "studentEnrollNo",
#                 "studentDoj",
#                 "studentCourseDuration",
#                 "studentFees",
#                 "studentDiscount",
#                 "studentRemark",
#                 "status",
#             ]
#         )
#         return redirect("manageStudent")
#     return render(request, "editStudent.html", {"students": students})


# def search_query(request):
#     query = request.GET.get("search") if request.GET.get("search") != None else ""
#     students = Student.objects.filter(
#         Q(studentName__icontains=query)
#         | Q(studentEnrollNo__icontains=query)
#         | Q(status__icontains=query)
#         | Q(studentPhno__icontains=query)
#         | Q(studentEmail__icontains=query)
#         | Q(studentEnrolledin__icontains=query)
#     )
#     return render(request, "search_query.html", {"students": students})


# def staff_search_query(request):
#     query = request.GET.get("search") if request.GET.get("search") != None else ""
#     staffs = Staff.objects.filter(
#         Q(staffName__icontains=query)
#         | Q(staffName__icontains=query)
#         | Q(staffEmail__icontains=query)
#         | Q(staffPhNo__icontains=query)
#         | Q(staffCourse__icontains=query)
#         | Q(UserName__icontains=query)
#         | Q(UserRule__icontains=query)
#     )
#     return render(request, "staff_search_query.html", {"staffs": staffs})


# def page_not_found_view(request, exception):
#     return render(request, "error404.html", status=404)


# def server_error(request):
#     return render(request, "servererror.html", status=500)
