from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from .models import StaffData
from django.contrib.auth import login,authenticate
from django.contrib.auth.hashers import check_password,make_password
# Create your views here.
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

class login_usr(generic.View):
    template_name = 'login.html'
    def post(self,request):
        UserName = request.POST.get("UserName")
        password = request.POST.get("Password")
        try:
            user = StaffData.objects.get(UserName=UserName)
            user = authenticate(UserName=UserName,password=password)
            if user is not None:
                print(user.UserRule)
                if user.UserRule != "null" and "2" == user.UserRule:
                    # messages.success(request, "Logged as Staff")
                    url = "staffPanel/{}".format(user.id)
                    return redirect(url)
                elif "1" == user.UserRule:
                    # messages.success(request, "Logged as Admin")
                    return redirect("adminPanel", id=user.id)
            else:
                messages.error(request, "Password Not Matched")
                return render(request, "login.html")

        except Staff.DoesNotExist:
            messages.error(request, "User Not Found")
            return render(request, "login.html")

    return render(request, "login.html")