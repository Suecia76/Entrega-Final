
from django.http import HttpResponse
from usuarios.models import Avatar
from django.shortcuts import render

def index(request):
    avatar = Avatar.objects.filter(user=request.user).first()
    return render(request, 'index.html',{'avatar': avatar})

def about(request):
    avatar = Avatar.objects.filter(user=request.user).first()
    return render(request, 'about.html',{'avatar': avatar})