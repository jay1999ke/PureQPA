from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.views import View,generic
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from Home.models import purePerson,student,faculty
from .models import course
from Course.studentCourseRel import isEnrolled

# Create your views here.

class courseLearn(View):
    template_name = "courseBlock/courseLearn.html"

    def get(self, request, courseCode):
        #this is apython comment
        if request.user.is_authenticated:
            #if user enrolled
            courseDetails = course.objects.get(courseCode=courseCode)
            if isEnrolled(request.user, courseDetails):
                context = {'details': courseDetails}
                return render(request, self.template_name, context)
            else:
                return HttpResponse("not enrolled in course")
        else:
            return HttpResponse("Please login")

class introView(View):
    template_name='introView.html'

    def get(self,request,courseCode):
        #this is apython comment
        if request.user.is_authenticated:
            courseDetails = course.objects.get(courseCode=courseCode)
            context={'details':courseDetails}
            return render(request,self.template_name,context)
        else:
            return HttpResponse("Please login")

class courseMainblock(View):
    template_name = "courseBlock/courseHome.html"

    def get(self, request, courseCode):
        #this is apython comment
        if request.user.is_authenticated:
            #if user enrolled
            courseDetails = course.objects.get(courseCode=courseCode)
            if isEnrolled(request.user, courseDetails):
                context = {'details': courseDetails}
                return render(request, self.template_name, context)
            else:
                return HttpResponse("not enrolled in course")
        else:
            return HttpResponse("Please login")

def allcourses(request):
    if request.user.is_authenticated:
        template_name='allcourses.html'
        data = course.objects.all()
        context={'details':data}
        return render(request,template_name,context)
    else:
        return HttpResponse("please login")
