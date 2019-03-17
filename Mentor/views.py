from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View, generic
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from Home.models import purePerson, student, faculty, pureAdmin
from Course.models import course, question, questionPaper
from Course.studentCourseRel import isEnrolled, isFaculty, getPerson
from .forms import *
from hashlib import sha1

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
        courseDetails = course.objects.get(courseCode=courseCode)
        if request.POST['submit'] == 'Start':
            marksForm = marks(request.POST)
            if marksForm.is_valid():
                totalMarks=int(marksForm.cleaned_data['totalMarks'])
                examName = marksForm.cleaned_data['name']
                r = sha1(examName.encode())
                new_exam = questionPaper(marks=totalMarks,course=courseDetails,examName=examName,examhash=r.hexdigest())
                curr_marks = 0
                #allQuestions = question.objects.filter(course=courseDetails)
                new_exam.save()

                return HttpResponseRedirect("/faculty/examcreation/"+str(courseCode)+"/"+str(r.hexdigest())+"/0")

class addExamQuestions(View):
    def get(self,request,courseCode,testhash,curr_marks):
        user = getPerson(request.user)

        if user.type == "faculty":
            #exam = questionPaper.objects.get(examhash = testhash)
            typeForm = questionType()
            courseDetails = course.objects.get(courseCode=courseCode)

            context = {'details': courseDetails,'form':typeForm}
            
            return render(request,"courseMentorBlock/addExamQuestionType.html",context=context)
        return HttpResponseRedirect("accounts/dashboard")

    def post(self,request,courseCode,testhash,curr_marks):
        typeForm = questionType(request.POST)

        if typeForm.is_valid():
            type_q = typeForm.cleaned_data['type']
            typehash = type_q
            return HttpResponseRedirect("/faculty/examquestion/"+courseCode+"/"+testhash+"/"+str(curr_marks)+"/"+typehash)

class addSelectedExamQuestions(View):
    def get(self,request,courseCode,testhash,curr_marks,typehash):

        testhash=str(testhash)
        exam = questionPaper.objects.get(examhash=testhash)
        exam_que = exam.questions.all()

        courseDetails = course.objects.get(courseCode=courseCode)
        type_q = typehash
        possible_q = question.objects.filter(course=courseDetails,type=type_q)
        possible_q = [(x,str(x)) for x in possible_q if (x not in exam_que)]
        possible_q = tuple(possible_q)
        que = questionSelect(possible_q=possible_q)
        context = {'details':courseDetails,'form':que}
        if len(possible_q) != 0:
            return render(request,"courseMentorBlock/addExamQuestion.html",context=context)
        else:
            return HttpResponseRedirect("/faculty/examcreation/"+str(courseCode)+"/"+str(testhash)+"/"+str(curr_marks))

    def post(self,request,courseCode,testhash,curr_marks,typehash):

        try:
            que_str = request.POST['question'].split(" | ")
            que_str = que_str[1]
            que_test = question.objects.get(question=que_str)
            testhash=str(testhash)
            exam = questionPaper.objects.get(examhash=testhash)
            curr_marks = int(curr_marks)
            marks = que_test.marks
            if(curr_marks < curr_marks + marks):        
                exam.questions.add(que_test)
                curr_marks = curr_marks + marks
                exam.status = curr_marks
                exam.save()
                return HttpResponseRedirect("/faculty/examcreation/"+str(courseCode)+"/"+str(testhash)+"/"+str(curr_marks))

        except:
            HttpResponseRedirect("/faculty/examcreation/"+str(courseCode)+"/"+str(testhash)+"/"+str(curr_marks))

class addQuestions(View):
    def get(self,request,courseCode):
        user = getPerson(request.user)

        if user.type == "faculty":
            #exam = questionPaper.objects.get(examhash = testhash)
            typeForm = addQuestion()
            courseDetails = course.objects.get(courseCode=courseCode)

            context = {'details': courseDetails,'form':typeForm}
            
            return render(request,"courseMentorBlock/addQuestion.html",context=context)
        return HttpResponseRedirect("accounts/dashboard")
    
    def post(self,request,courseCode):
        typeForm = addQuestion(request.POST)
        if typeForm.is_valid():
            type_q = typeForm.cleaned_data['type']
            print("\n\n\n\n\n\n",type_q)
            if type_q == "manual":
                return HttpResponseRedirect("/faculty/resources/"+courseCode+"/addQuestion/manual")
            elif type_q == "auto":
                return HttpResponseRedirect("/faculty/resources/"+courseCode+"/addQuestion/auto")

class addQuestionsManual(View):
    def get(self,request,courseCode):
        return HttpResponse("Working in progress")
    
    def post(self,request,courseCode):
        pass

class addQuestionsAuto(View):
    def get(self,request,courseCode):
        pass
    
    def post(self,request,courseCode):
        pass