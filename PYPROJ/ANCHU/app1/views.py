from django.shortcuts import render
from django.http import HttpResponse # print
from .models import Database

# Create your views here.
# functions
def hello(request):
    return HttpResponse("HELLO WORLD")
def home(request):
    return HttpResponse("fIRST pROJECT")
def python(request):
    return render (request,'hello.html')
def anchu(request):
    return render(request, 'anchu.html', {'name':'Anchu'})
def fun(request):
    data= Database.objects.all()
    return render(request, 'anchu.html',{'name':data})