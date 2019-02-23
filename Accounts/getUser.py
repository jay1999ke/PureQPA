from Home.models import purePerson,student,faculty
from django.contrib.auth.models import User

def getStudent(user):
    this_person=purePerson.objects.get(user=user)
    this_student = student.objects.get(pPerson=this_person)
    return this_student


def getFaculty(user):
    this_person = purePerson.objects.get(user=user)
    this_faculty = faculty.objects.get(pPerson=this_person)
    return this_faculty
