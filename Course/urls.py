from django.urls import path
from . import views

urlpatterns = [
    path('home/<slug:courseCode>',views.introView.as_view(),name='intro'),
    path('block/<slug:courseCode>',views.courseMainblock.as_view(),name='courseBlock'),
    path('allcourses',views.allcourses,name='allcourses'),
    path('block/<slug:courseCode>/exam',views.courseExam.as_view(),name="learn"),
    path('block/<slug:courseCode>/exam/<slug:examhash>/<int:questionnumber>/<int:marks>',views.takeExam.as_view(),name="exam_q"),
]
