from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.views import View,generic
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from Home.models import purePerson,student,faculty
from .models import course, question, questionPaper
from Course.studentCourseRel import isEnrolled
from .forms import examSelect

# Create your views here.

class courseExam(View):
    template_name = "courseBlock/courseExam.html"

    def get(self, request, courseCode):
        #this is apython comment
        if request.user.is_authenticated:
            #if user enrolled
            courseDetails = course.objects.get(courseCode=courseCode)
            if isEnrolled(request.user, courseDetails):
                context = {'details': courseDetails}

                all_exams = questionPaper.objects.filter(course=courseDetails,launchStatus=True)

                all_exams = [(x,str(x)) for x in all_exams]

                select_exam_form= examSelect(all_exams)

                context['form'] = select_exam_form

                return render(request, self.template_name, context)
            else:
                return HttpResponse("not enrolled in course")
        else:
            return HttpResponse("Please login")
        
    def post(self, request, courseCode):
        courseDetails = course.objects.get(courseCode=courseCode)
        if isEnrolled(request.user, courseDetails):
            exam = questionPaper.objects.get(course=courseDetails,examName=request.POST['exam'])
            redirect_str = "exam/"+exam.examhash +"/"+str(0)+"/"+str(0)
            return HttpResponseRedirect(redirect_str)
       
class takeExam(View):
    template_name = "courseBlock/examQuestions.html"

    def get(self,request,courseCode,examhash,questionnumber):
        return HttpResponse("sdfg")

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
