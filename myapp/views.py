from django.shortcuts import render
from django.http import HttpResponse
import mysql.connector

from django.http import JsonResponse
from django.core.serializers import serialize
from .models import Country

def home(request):
    return render(request, 'home.html')

