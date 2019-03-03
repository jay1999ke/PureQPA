from django.urls import path
from . import views

urlpatterns = [
    path('', views.test),
    path('dashboard',views.dashboard.as_view(),name="fac_dash"),
    path('test',views.test),
    path('block/<slug:courseCode>',views.mentorCourseHome.as_view(),name='courseBlock'),
    path('create/exam/<slug:courseCode>',views.createExam.as_view(),name="create_exam"),

]
