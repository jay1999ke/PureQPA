from django import forms
from django.contrib.auth.models import User
from Home.models import student, faculty, pureAdmin, purePerson
from Course.models import question,questionPaper, course

class marks(forms.Form):
    name = forms.CharField()
    totalMarks = forms.IntegerField()



class questionType(forms.Form):
    types=[('binary','Binary question'),
        ('wh','Wh type question')]
    type=forms.ChoiceField(choices=types)


class questionSelect(forms.Form):
    def __init__(self, possible_q,*args, **kwargs):
        super(questionSelect, self).__init__(*args, **kwargs)
        self.fields['question'] = forms.ChoiceField(choices=possible_q)

class addQuestion(forms.Form):
    types=[
        ('auto','Generate Questions')]
    type= forms.ChoiceField(choices=types)

class autoGenerate(forms.Form):
    text = forms.CharField(widget=forms.Textarea)

class questionSelectAuto(forms.Form):
    def __init__(self,questions,*args,**kwargs):
        super(questionSelectAuto,self).__init__(*args, **kwargs)
       
        self.fields['possible_qs'] = forms.MultipleChoiceField(choices=questions,widget  = forms.CheckboxSelectMultiple)

class questionSelectAutoFinal(forms.Form):
    answer = forms.CharField()
    marks = forms.IntegerField()
    types=(('binary','binary'),
        ('wh','wh')
    )
    type=forms.ChoiceField(choices=types)



