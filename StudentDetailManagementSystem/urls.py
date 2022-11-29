from django.urls import path, include

urlpatterns = [
    # path("admin/", admin.site.urls),
    path("", include("StaffLogin.urls")),
    path("", include("StudentData.urls")),
]
