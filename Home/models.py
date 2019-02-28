from django.db import models
from Course.models import course
from django.contrib.auth.models import User

# Create your models here.zz
class purePerson(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    types=(
        ('student','student'),
        ('faculty','faculty'),
        ('pureAdmin','pureAdmin'),
    )
    type=models.CharField(max_length=20, choices=types, default='student')


    def __str__(self):
        return self.user.first_name+" "+self.user.last_name

class student(models.Model):
    pPerson= models.OneToOneField(purePerson, on_delete=models.CASCADE)
    roll=models.CharField(max_length=8)
    year=models.IntegerField()
    coursesTaken=models.ManyToManyField(course,related_name='course_instudents')

    def __str__(self):
        return self.pPerson.user.first_name+" "+self.pPerson.user.last_name

class faculty(models.Model):
    pPerson = models.OneToOneField(purePerson, on_delete=models.CASCADE)
    idNum=models.CharField(max_length=8)
    yrEmployed=models.IntegerField()
    designation =models.CharField(max_length=64,default="")
    courses=models.ManyToManyField(course,related_name='course_faculties')

    def __str__(self):
        return self.pPerson.user.first_name+" "+self.pPerson.user.last_name

class pureAdmin(models.Model):
    pPerson = models.OneToOneField(purePerson, on_delete=models.CASCADE)
    adminusername=models.CharField(max_length=16)
    adminpasscode=models.CharField(max_length=16)

    def __str__(self):
        return self.pPerson.user.first_name
        
class department(models.Model):
    deptname=models.CharField(max_length=64)
    #hod=models.ForeignKey(faculty,on_delete = models.CASCADE,blank=True)
    #coursesprovided=models.ManyToManyField(course,blank=True,related_name='dept_courses')

    def __str__(self):
        return self.deptname

