from django.urls import path
from . import views

urlpatterns = [
    path('', views.test),
    path('dashboard',views.dashboardAdmin.as_view(),name="admin_dash"),
    path('test',views.test),
    path('block/<slug:courseCode>',views.AdminHome.as_view(),name='courseBlock'),


]
