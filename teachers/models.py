from django.db import models

# Create your models here.

class TeacherInfo(models.Model):
    
    staff_number = models.CharField(max_length=8)
    last_name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    levels = models.CharField(max_length=8)
    class_held = models.CharField(max_length=5, blank=True, null=True)
    game = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.last_name

