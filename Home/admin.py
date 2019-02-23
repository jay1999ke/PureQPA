from django.contrib import admin
from .models import purePerson,student,department,pureAdmin,faculty

# Register your models here.
admin.site.register(purePerson)
admin.site.register(student)
admin.site.register(department)
admin.site.register(pureAdmin)
admin.site.register(faculty)
