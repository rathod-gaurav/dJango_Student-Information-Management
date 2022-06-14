from django import forms
from .models import *

class AddStudentForm(forms.ModelForm):
    class Meta:
        model = StudentProfile
        fields = ['name', 'roll_no', 'department', 'hostel']