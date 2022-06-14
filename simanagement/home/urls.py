from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('add-student', add_student, name='add_student'),
    path('student-delete/<id>', student_delete, name='student_delete'),
    path('student-update/<id>', student_update, name='student_update'),
    path('upload-json', upload_json, name='upload_json'),
]