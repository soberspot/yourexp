from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# from django.shortcuts import render

def index(request):
    return render(request, "index.html")

# def index(request):
#     return HttpResponse("Hello World!")
