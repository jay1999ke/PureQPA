from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.views import View,generic
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.hashers import make_password
from Home.models import purePerson,student,faculty
from . import forms
from Course.models import course
from .getUser import getFaculty,getStudent

# Create your views here.
def index(request):
    return render(request,'login.html')

def dashboard(request):
    if request.user.is_authenticated:
        return render(request,'loginDash.html')
    else:
        return HttpResponse("failed")

class loginUser(View):
    template_name='login.html'

    def get(self,request):
        #login for facuty remaining
        if request.user.is_authenticated == True:
            person = purePerson.objects.get(user=request.user)
            if person.type == 'student':
                activeUser = student.objects.get(pPerson=person)
            elif person.type =='faculty':
                activeUser = faculty.objects.get(pPerson=person)
            else :
                activeUser = user
            if request.user.is_active and person.type == 'student': #only for students
                courses_taken = activeUser.coursesTaken.all()
                context = {'iduser': [activeUser, person.type, request.user.last_name, request.user.first_name,
                                      request.user.email], 'name': request.user.first_name, 'courses_taken': courses_taken}
                redirect_template = 'loginDash.html'
                return render(request,redirect_template,context)
            elif request.user.is_active and person.type =='faculty':
                return HttpResponseRedirect('/faculty/dashboard')

        else:
            return render(request,self.template_name)

    def post(self,request):
        username = request.POST.get('username','')
        password = request.POST.get('password','')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user) #the user is now logged in
                return HttpResponseRedirect('/accounts/dashboard')
        else:
            return HttpResponse("login failed")

class logoutUser(View):
    def post(self,request):
        logout(request)
        return redirect('/accounts/login')

class registerStudent(View):
    template_name='registerStudent.html'

    def get(self,request):
        form = forms.registerStudentForm()
        return render(request,self.template_name,{'form':form})

    def post(self,request):
        form = forms.registerStudentForm(request.POST)
        if form.is_valid() and form.cleaned_data['password']==form.cleaned_data['passwordAgain'] :
            username=form.cleaned_data['username']
            try:
                User.objects.get(username=username)
                return HttpResponse("username exists")
            except:
                password=form.cleaned_data['password']
                password=make_password(password, salt=None, hasher='default')
                first_name=form.cleaned_data['first_name']
                last_name=form.cleaned_data['last_name']
                email=form.cleaned_data['email']
                roll=form.cleaned_data['roll']
                year=form.cleaned_data['year']
                user = User(username=username,password=password,first_name=first_name,last_name=last_name,email=email)
                user.save()
                person = purePerson(user=user)
                person.save()
                stu = student(pPerson=person,roll=roll,year=year)
                stu.save()
                return HttpResponse("success")
        else:
            return HttpResponse("failed reg")

class courseEnroll(View):

    def post(self,request,courseCode):
        this_student = getStudent(request.user)
        this_course = course.objects.get(courseCode=courseCode)
        this_student.coursesTaken.add(this_course)
        return redirect('/accounts/dashboard')

    def get(self,request,*args,**kwargs):
        return HttpResponse("dont try to hack, we're still underdevelopment")
