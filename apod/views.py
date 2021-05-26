from django.shortcuts import render

# Create your views here.

def apod(request):
    return render(request, 'apod.html', {})
