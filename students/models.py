from django.db import models

# Create your models here.

class StudentInfo(models.Model):
    student_number = models.CharField(max_length=8)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    level = models.CharField(max_length=5, null=False)
    game = models.CharField(max_length=50, blank=True, null=True)


    def __str__(self):
        return self.first_name





