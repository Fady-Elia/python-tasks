from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()

    def __str__(self):
        return self.name

class Course(models.Model):
    name = models.CharField(max_length=100)
    instructor = models.CharField(max_length=100)
    students = models.ManyToManyField(Student)

    def __str__(self):
        return self.name

