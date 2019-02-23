from django.urls import path
from . import views

urlpatterns = [
    path('login',views.loginUser.as_view(),name='login'),
    path('logintest',views.loginUser.as_view(),name='logintest'),
    path('dashboard',views.loginUser.as_view(),name='dashboard'),
    path('register/student',views.registerStudent.as_view(),name='registerStudent'),#for now 
    path('courseEnroll/<slug:courseCode>',views.courseEnroll.as_view(),name='courseEnroll'),
    path('logout',views.logoutUser.as_view(),name='logout'),
]
