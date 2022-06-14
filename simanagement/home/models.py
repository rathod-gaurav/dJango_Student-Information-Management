from django.db import models

# Create your models here.
class StudentProfile(models.Model):
    name = models.CharField(max_length=20)
    roll_no = models.IntegerField()
    department = models.CharField(max_length=50)
    hostel = models.CharField(max_length=20)

    def __str__(self):
        return self.name