
from django.db import models

class Student(models.Model):
    student_id = models.CharField(max_length=20)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=20)
    date_of_birth = models.DateField()
    contact_no = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.student_id} - {self.first_name} {self.last_name}"

    