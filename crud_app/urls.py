from django.urls import path, include
from django.contrib.auth.decorators import login_required
from . import views

urlpatterns = [
    path('',views.index, name="home"),
    path("login/", views.login_view, name="login"),
    path("otp_verify/", views.otp_verify, name="otp_verify"),
    path("logout/", views.logout_view, name="logout"),
    path("show/", views.show,name="show"),
    path("delete/<emp_id>", views.delete_data, name="delete"),
    path("edit/<emp_id>", views.edit_data, name="edit")
]



