from django.urls import path
from . import views

urlpatterns = [
    path('home/<slug:courseCode>',views.introView.as_view(),name='intro'),
    path('block/<slug:courseCode>',views.courseMainblock.as_view(),name='courseBlock'),
    path('allcourses',views.allcourses,name='allcourses'),
    path('block/<slug:courseCode>/learn',views.courseLearn.as_view(),name="learn"),
]
