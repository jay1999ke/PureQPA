from django.db import models

# Create your models here.

class course(models.Model):
    coursekey = models.CharField(max_length=8)
    courseCode = models.CharField(max_length=8)
    name=models.CharField(max_length=128)
    link=models.CharField(max_length=512)

    def __str__(self):
        return self.name


class question(models.Model):
    course=models.ForeignKey(course,related_name='course_question',on_delete=models.CASCADE)
    question = models.CharField(max_length=1024)
    topic = models.CharField(max_length=128)
    marks = models.IntegerField()
    types=(
        ('binary','binary'),
        ('blank','blank'),
        ('wh','wh'),
    )
    type=models.CharField(max_length=20, choices=types, default='binary')


    def __str__(self):
        return self.course.courseCode + " | " + self.question + " | " + str(self.marks) +" marks"

class questionPaper(models.Model):
    course=models.ForeignKey(course,related_name='course_question_paper',on_delete=models.CASCADE)
    questions =models.ManyToManyField(question,related_name='question_of_course')
    examName = models.CharField(max_length=1024)

    def __str__(self):
        return self.examName