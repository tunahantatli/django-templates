from django.shortcuts import render
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
    context = {
        'form': form
    }
    return render(request, 'students/student_add.html', context)