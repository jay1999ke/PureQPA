from django.urls import path
from . import views

urlpatterns = [
    path('', views.test),
    path('dashboard',views.dashboard.as_view(),name="fac_dash"),
    path('test',views.test),

]
