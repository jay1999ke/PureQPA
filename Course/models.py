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
        ('wh','wh'),
    )
    answer = models.CharField(max_length=1024,default=True)
    type=models.CharField(max_length=20, choices=types, default='binary')

    def __str__(self):
        return self.course.courseCode + " | " + self.question + " | " + str(self.marks)

class questionPaper(models.Model):
    course=models.ForeignKey(course,related_name='course_question_paper',on_delete=models.CASCADE)
    questions =models.ManyToManyField(question,related_name='questions_of_paper')
    examName = models.CharField(max_length=1024)
    marks = models.IntegerField(default=0)
    examhash = models.CharField(max_length=40)
    status = models.IntegerField(default=-1)
    launchStatus = models.BooleanField(default=False)



    def __str__(self):
        return self.examName

