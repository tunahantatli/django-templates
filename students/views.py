from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    context = {
        'title': 'Tunahan Tatlı'
    }
    return render(request, 'students/home.html', context)
   # return HttpResponse('<h1>Hello</h1>')
