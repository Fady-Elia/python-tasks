from django.shortcuts import render
from myapp.models import Student, Course

def index(request):
    students = Student.objects.all()
    courses = Course.objects.all()
    context = {
        'students': students,
        'courses': courses,
    }
    return render(request, 'index.html', context)

