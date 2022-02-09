from django.contrib import admin
from app2_1.models import Person
from app2_1.models import Student
from app2_1.models import Staff

# Register your models here.
admin.site.register(Person)
admin.site.register(Student)
admin.site.register(Staff)

