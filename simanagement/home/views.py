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

def upload_json(request):
    context ={'form': UploadJSONForm}
    try:
        if request.method=='POST':
            form = UploadJSONForm(request.POST)
            json_file = request.FILES['file']

            if form.is_valid():
                JsonUpload.objects.create(file=json_file)
            
            # file = JsonUpload.objects.get(file=json_file)
            print("okay")
            # f = open(json_file)
            
            # data = json.load(f)
            # print(data)

            return redirect('/')
    except Exception as e:
        print(e)
    return render(request, 'upload_json.html', context)