from unicodedata import name
from django.shortcuts import render, redirect
from .models import *
from .forms import AddStudentForm, UploadJSONForm
import json
# Create your views here.

def home(request):
    context = {'students': StudentProfile.objects.all()}
    return render(request, 'home.html', context)

def add_student(request):
    context = {'form': AddStudentForm}
    try:
        if request.method=='POST':
            form = AddStudentForm(request.POST)
            name = request.POST.get('name')
            roll_no = request.POST.get('roll_no')
            department = request.POST.get('department')
            hostel = request.POST.get('hostel')

            if form.is_valid():
                StudentProfile.objects.create(
                    name=name, roll_no=roll_no, department=department, hostel=hostel,
                )
            return redirect('/')
    except Exception as e:
        print(e)
    return render(request, 'add_student.html', context)

def student_delete(request, id):
    try:
        student = StudentProfile.objects.get(id=id)
        student.delete()
    except Exception as e:
        print(e)
    return redirect('/')

def student_update(request, id):
    context = {}
    try:
        student = StudentProfile.objects.get(id=id)
        initial_dict = {'name': student.name, 'roll_no':student.roll_no, 'department':student.department, 'hostel':student.hostel}

        form = AddStudentForm(initial=initial_dict)

        if request.method=='POST':
            form = AddStudentForm(request.POST)
            student.name = request.POST.get('name')
            student.roll_no = request.POST.get('roll_no')
            student.department = request.POST.get('department')
            student.hostel = request.POST.get('hostel')

            if form.is_valid():
                student.save()
            return redirect('/')
        
        context['form']=form
    except Exception as e:
        print(e)
    return render(request, 'student_update.html', context)

import json
import pandas as pd
from django.conf import settings
def handle_uploaded_file(file_path):
    file_path = settings.MEDIA_ROOT + file_path[6:]
    # print(file_path)
    if file_path[-4:] == '.csv':
        df = pd.read_csv(file_path)
        for NAME, ROLL_NO, DEPARTMENT, HOSTEL in zip(df.name, df.roll_no, df.department, df.hostel):
            models = StudentProfile(name=NAME, roll_no=ROLL_NO, department=DEPARTMENT, hostel=HOSTEL)
            models.save()
    elif file_path[-4:] == 'json':
        with open(file_path) as f:
            students_list = json.load(f)
        for student in students_list:
            StudentProfile.objects.create(
                name=student["name"], roll_no = student["roll_no"], department=student["department"], hostel=student["hostel"]
                )


def upload_json(request):
    context ={'form': UploadJSONForm}
    try:
        if request.method=='POST':
            form = UploadJSONForm(request.POST)
            json_file = request.FILES['file']

            if form.is_valid():
                file_obj = JsonUpload.objects.create(file=json_file)
                file_path = '/media/'+ str(file_obj.file)
                # print(file_path)
                handle_uploaded_file(file_path)
            
            # print('okay again')

            return redirect('/')
    except Exception as e:
        print(e)
    return render(request, 'upload_json.html', context)