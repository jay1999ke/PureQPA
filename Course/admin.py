from django.contrib import admin
from .models import course,question,questionPaper,intermediateQuestion

# Register your models here.
admin.site.register(course)
admin.site.register(question)
admin.site.register(questionPaper)
admin.site.register(intermediateQuestion)