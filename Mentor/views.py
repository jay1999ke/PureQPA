from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View, generic
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from Home.models import purePerson, student, faculty
from Course.models import course
from Course.studentCourseRel import isEnrolled

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
                s = "stu"
                if activeUser.faculty_access:
                    s = "fac"
            elif person.type == 'faculty':
                activeUser = faculty.objects.get(pPerson=person)
                s = "fac"
            else:
                activeUser = user
            if request.user.is_active :  # only for students
                if s == "stu": 
                    """courses_taken = activeUser.coursesTaken.all()
                    context = {'iduser': [activeUser, person.type, request.user.last_name, request.user.first_name,
                                        request.user.email], 'name': request.user.first_name, 'courses_taken': courses_taken}
                    redirect_template = 'loginDash.html'
                    return render(request, redirect_template, context)
                    """
                    return HttpResponseRedirect('/accounts/dashboard')
                elif s == "fac":
                    return HttpResponse("you are faculty member")
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
