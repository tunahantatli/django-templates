from django.shortcuts import render
from django.http import HttpResponse
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
