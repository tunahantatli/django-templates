from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse

from .models import Student
from .forms import StudentForm
# Create your views here.
def home(request):
    context = {
        'title': 'Tunahan Tatlı',
        'description': 'This is a description. The code write by human',
        'number': 125637849,
        'list': ['hello', 'this', 'is', 'a', 'list', ['arif','fivefivefiveDotcom','gora']],
        'e_list':[
            {'name': 'selim', 'age':45},
            {'name': 'ali', 'age':27},
            {'name': 'veli', 'age':62},
            {'name': 'salim', 'age':24}
        ],
    }
    return render(request, 'students/home.html', context)
   # return HttpResponse('<h1>Hello</h1>')

def student_list(request):
    students = Student.objects.all()
    context = {
        'students': students
    }
    return render(request, 'students/student_list.html', context)


def student_add(request):
    form = StudentForm()
    if request.method == 'POST':
        print('POST :', request.POST)
        print('files :', request.FILES)
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    context = {
        'form': form
    }
    return render(request, 'students/student_add.html', context)

def student_update(request, id):
    student = get_object_or_404(Student, id=id)
    form = StudentForm(instance=student)
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    context = {
        'form': form
    }
    return render(request, 'students/student_update.html', context)

def student_detail(request, id):
    student = get_object_or_404(Student, id=id)
    context = {
        'student': student
    }
    return render(request, 'students/student_detail.html', context)

def student_delete(request, id):
    student = get_object_or_404(Student, id=id)

    if request.method == 'POST':
        student.delete()
        return redirect('student_list')
    context = {
        'student': student
    }
    return render(request, 'students/student_delete.html', context)