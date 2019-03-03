from django import forms
from django.contrib.auth.models import User
from Home.models import student, faculty, pureAdmin, purePerson
from Course.models import question,questionPaper, course

class marks(forms.Form):
    name = forms.CharField()
    totalMarks = forms.IntegerField()


