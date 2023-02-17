from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    context = {
        'title': 'Tunahan Tatlı',
        'description': 'This is a description. The code write by human',
        'number': 125637849,
        'list': ['hello', 'this', 'is', 'a', 'list', ['arif','fivefivefiveDotcom','gora']],
    }
    return render(request, 'students/home.html', context)
   # return HttpResponse('<h1>Hello</h1>')
