from django.shortcuts import render

# Create your views here.
from .models import Course

def index(request):
    courses = Course.objects.all()
    template_name = 'courses/index.html'
    #contexto = compact do php
    context = {
        'courses': courses
    }
    return render(request, template_name, context)
