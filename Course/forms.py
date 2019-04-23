from django import forms
from django.contrib.auth.models import User
from Home.models import student, faculty, pureAdmin, purePerson
from Course.models import question,questionPaper, course

class examSelect(forms.Form):
    def __init__(self, all_exams,*args, **kwargs):
        super(examSelect, self).__init__(*args, **kwargs)
        self.fields['exam'] = forms.ChoiceField(choices=all_exams)

class binaryAnswer(forms.Form):
    choice=[('True','True'),
        ('False','false')]
    ans= forms.ChoiceField(choices=choice)

class singleWordAnswer(forms.Form):
    ans = forms.CharField()


