from django.shortcuts import render
from django.shortcuts import HttpResponse
# Create your views here.


def index(request):
    context_dict = {'boldmessage':"I am from context"}
    return render(request, '/rango/index.html', context_dict)