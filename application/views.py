from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from rest_framework import viewsets
from .models import *
from .serializers import *

# Create your views here.
def index(request, path=None):
    return render(request, 'index.html')



class WindViewSet(viewsets.ModelViewSet):
    queryset = WindSpeed.objects.all()
    serializer_class = WindSerializer
