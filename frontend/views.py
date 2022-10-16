from django.shortcuts import render


from rest_framework.decorators import api_view
from rest_framework.response import Response


# Create your views here.
def list(request):
    return render(request, 'frontend/list.html')

def led(request):
    return render(request, 'frontend/led.html')