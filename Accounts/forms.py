from django import forms
from django.contrib.auth.models import User
from Home.models import student

class registerUserForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField(max_length=32, widget=forms.PasswordInput)
    passwordAgain=forms.CharField(max_length=32, widget=forms.PasswordInput)
    first_name=forms.CharField()
    last_name=forms.CharField()
    email=forms.EmailField()

    class Meta:
        model = User
        fields =('username','password','first_name','last_name','email')

class registerStudentForm(registerUserForm):
    roll = forms.CharField()
    year = forms.CharField()

    class Meta:
        model = student
        fields =('username','password','first_name','last_name','email','roll','year')
