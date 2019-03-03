from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View, generic
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from Home.models import purePerson, student, faculty, pureAdmin
from Course.models import course
from Course.studentCourseRel import isEnrolled, isFaculty, getPerson
from .forms import marks

# Create your views here.

def test(request):
    return render(request,'postFacLoginBase.html')


class dashboard(View):
    template_name = 'login.html'

    def get(self, request):
        #login for facuty remaining
        if request.user.is_authenticated == True:
            person = purePerson.objects.get(user=request.user)
            if person.type == 'student':
                activeUser = student.objects.get(pPerson=person)
            elif person.type == 'faculty':
                activeUser = faculty.objects.get(pPerson=person)
            elif person.type == 'pureAdmin':
                activeUser = pureAdmin.objects.get(pPerson=person)
            else:
                activeUser = user
            if request.user.is_active :  # only for students
                if person.type =='student': 
                    return HttpResponseRedirect('/accounts/dashboard')
                elif person.type =='faculty':
                    courses = activeUser.courses.all()
                    context = {'iduser': [activeUser, person.type, request.user.last_name, request.user.first_name,
                                      request.user.email], 'name': request.user.first_name, 'courses': courses}
                    print(context)
                    return render(request,"dashboard.html",context)
                elif person.type == 'pureAdmin':
                    return HttpResponseRedirect('/admin/dashboard')
        else:
            return HttpResponseRedirect('/accounts/login')

    def post(self, request):
        """
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)  # the user is now logged in
                return HttpResponseRedirect('/accounts/dashboard')
        else:
            return HttpResponse("login failed")
        """
        pass

class mentorCourseHome(View):
    template_name = "courseMentorBlock/courseHome.html"

    def get(self, request, courseCode):
        #this is apython comment
        if request.user.is_authenticated:
            #if user enrolled
            try:
                courseDetails = course.objects.get(courseCode=courseCode)
                if isFaculty(request.user, courseDetails):
                    context = {'details': courseDetails}
                    return render(request, self.template_name, context)
                else:
                    return HttpResponse("not a faculty in course")
            except:
                return HttpResponseRedirect('/accounts/dashboard')
            
        else:
            return HttpResponse("Please login")

class createExam(View):
    
    def get(self, request,courseCode):
        user = getPerson(request.user)

        if user.type == "faculty":
            courseDetails = course.objects.get(courseCode=courseCode)
            template_name = "courseMentorBlock/createExam.html"
            marksForm = marks()
            context = {'details': courseDetails,'form':marksForm}
            return render(request,template_name,context)
        else : 
            return HttpResponseRedirect('/accounts/login')

    def post(self,request,courseCode):
        return HttpResponse("")
