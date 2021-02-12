from django.db import models

# Create your models here.


class Sandt(models.Model):
    student_number = models.CharField(max_length=8)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    level = models.CharField(max_length=5, null=False)
    staff_number = models.CharField(max_length=8)
    teacher_full_name = models.CharField(max_length=80)
    game = models.TextField(blank=True, null=True)