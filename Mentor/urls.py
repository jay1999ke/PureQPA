from django.urls import path
from . import views

urlpatterns = [
    path('', views.test),
    path('dashboard',views.dashboard.as_view(),name="fac_dash"),
    path('test',views.test),
    path('block/<slug:courseCode>',views.mentorCourseHome.as_view(),name='courseBlock'),
    path('create/exam/<slug:courseCode>',views.createExam.as_view(),name="create_exam"),
    path('examcreation/<slug:courseCode>/<slug:testhash>/<int:curr_marks>',views.addExamQuestions.as_view(),name="add_questions"),
    path('examquestion/<slug:courseCode>/<slug:testhash>/<int:curr_marks>/<slug:typehash>',views.addSelectedExamQuestions.as_view(),name="add_questions"),
    path('resources/<slug:courseCode>/addQuestion',views.addQuestions.as_view(),name="add_q"),
    path('resources/<slug:courseCode>/addQuestion/manual',views.addQuestionsManual.as_view(),name="add_q_m"),
    path('resources/<slug:courseCode>/addQuestion/auto',views.addQuestionsAuto.as_view(),name="add_q_a"),
    path('resources/<slug:courseCode>/addQuestion/auto/<slug:hasher>',views.addQuestionsAutoFinal.as_view(),name="add_q_af"),
]
