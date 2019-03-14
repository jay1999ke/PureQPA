from django import forms
from django.contrib.auth.models import User
from Home.models import student, faculty, pureAdmin, purePerson
from Course.models import question,questionPaper, course

class marks(forms.Form):
    name = forms.CharField()
    totalMarks = forms.IntegerField()



class questionType(forms.Form):
    types=[('binary','Binary question'),
        ('blank','Fill in the blanks'),
        ('wh','Wh type question')]
    type=forms.ChoiceField(choices=types)


class questionSelect(forms.Form):
     
     def __init__(self, possible_q,*args, **kwargs):
        super(questionSelect, self).__init__(*args, **kwargs)
        self.fields['question'] = forms.ChoiceField(choices=possible_q)
