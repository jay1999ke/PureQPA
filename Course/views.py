from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.views import View,generic
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from Home.models import purePerson,student,faculty, scoreExam
from .models import course, question, questionPaper
from Course.studentCourseRel import isEnrolled, getStudent
from .forms import examSelect, singleWordAnswer, binaryAnswer

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
            redirect_str = "exam/"+exam.examhash +"/"+str(1)+"/"+str(0)
            return HttpResponseRedirect(redirect_str)
       
class takeExam(View):
    template_name = "courseBlock/examQuestions.html"

    def get(self,request,courseCode,examhash,questionnumber,marks):
        courseDetails = course.objects.get(courseCode=courseCode)
        exam = questionPaper.objects.get(examhash=examhash)
        questionnumber = int(questionnumber)
        questions = exam.questions.all()
        question = questions[questionnumber-1]
        context = {"question":question.question,"course":courseDetails,"qnum":questionnumber}
        if question.type == "wh":
            form = singleWordAnswer()
        else:
            form = binaryAnswer()
        
        context['form']=form
        context['details']=courseDetails
        
        return render(request,self.template_name,context=context)

    def post(self,request,courseCode,examhash,questionnumber,marks):
        form1 = singleWordAnswer(request.POST)
        form2 = binaryAnswer(request.POST)
        
        courseDetails = course.objects.get(courseCode=courseCode)
        exam = questionPaper.objects.get(examhash=examhash)
        questionnumber = int(questionnumber)
        questions = exam.questions.all()
        question = questions[questionnumber-1]
        marks = int(marks)
        correct = False


        if form1.is_valid():

            if(form1.cleaned_data['ans'] == question.answer):
                correct = True
        elif form2.is_valid():
            if(form2.cleaned_data['ans'] == question.answer):
                correct= True
        else:
            return HttpResponse("Internal server error: 500")

        if correct:
            marks += int(question.marks)

        if len(questions) == questionnumber:
            student= getStudent(request.user)
            score = scoreExam(student = student,question_paper = exam,score=marks,outof=exam.marks)
            score.save()
            str_score = str(marks) + " / " + str(exam.marks)
            context = {"exam":exam.examName,"score":str_score}
            context['details']=courseDetails
            return render(request,"courseBlock/showScore.html",context=context)
        else:
            return HttpResponseRedirect("/course/block/"+courseCode+"/exam/"+examhash+"/"+str(questionnumber+1)+"/"+str(marks))

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
