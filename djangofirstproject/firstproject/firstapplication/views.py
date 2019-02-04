from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    first_dict={'read':"HELLO I AM COMING FROM THE TEMPLATE TAGGING PAGE"}
    return render(request,'firstapplication/index.html',context=first_dict)
