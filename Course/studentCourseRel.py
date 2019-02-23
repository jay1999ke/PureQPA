from Home.models import purePerson, student, faculty
from django.contrib.auth.models import User
from .models import course


def getStudent(user):
    this_person = purePerson.objects.get(user=user)
    this_student = student.objects.get(pPerson=this_person)
    return this_student


def getFaculty(user):
    this_person = purePerson.objects.get(user=user)
    this_faculty = faculty.objects.get(pPerson=this_person)
    return this_faculty

def isEnrolled(user,courseTaken):
    studentUser = getStudent(user)
    if courseTaken in studentUser.coursesTaken.all():
        return True
    else:
        return False