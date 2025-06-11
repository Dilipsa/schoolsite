from django.db import models

class Course(models.Model):
    course_name = models.CharField(max_length=20)
    course_fee = models.CharField(max_length=10)

    def __str__(self):
        return self.course_name
    
class Student(models.Model):
    roll_no = models.CharField(max_length=5)
    name = models.CharField(max_length=20)
    course = models.ManyToManyField(Course)

    def __str__(self):
        return self.name
    
class Address(models.Model):
    state = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
