from django.shortcuts import render
from .forms import StudentRegistration
from .models import Student

from django.http import JsonResponse
import json
# from django.views.decorators.csrf import csrf_exempt
# Create your views here.
def home(request):
    form  = StudentRegistration
    student = Student.objects.all()
    context = {
        'form':form,
        'Students':student
    }
    return render (request,'home.html',context)

# @csrf_exempt # jaha per csrf ka protection nahi chahiye waha per use kare.
def save_data(request):
    if request.method == "POST":
        form = StudentRegistration(request.POST)
        if form.is_valid():
            studentid=request.POST.get('studentid')
            name=request.POST['name']
            email=request.POST['email']
            password=request.POST['password']

            if studentid == '':
                student = Student(name=name,email=email,password=password)
            else:
                student = Student(id=studentid, name=name,email=email,password=password)
            student.save()

            stu = Student.objects.values()
            # print(stu)
            student_data = list(stu)
            return JsonResponse({'status':"Save", 'student_data':student_data})
        else:
            return JsonResponse({'status':0})


def delete_data(request):
    if request.method == "POST":
        id = request.POST.get('sid')
        Student.objects.get(id=id).delete()
        return JsonResponse({'status':1})
    else:
        return JsonResponse({'status':0})

def edit_data(request):
    if request.method == "POST":
        id = request.POST.get('sid')
        student=Student.objects.get(id=id)

        # Convert the student data to a dictionary
        student_data = {
            'id': student.id,
            'name': student.name,
            'email': student.email,
            'password': student.password,
        }
        return JsonResponse(student_data)
    else:
        return JsonResponse({'status':0})