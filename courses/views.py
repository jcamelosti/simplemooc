from django.shortcuts import render, get_object_or_404

# Create your views here.
from .models import Course


def index(request):
    courses = Course.objects.all()
    template_name = 'courses/index.html'
    # contexto = compact do php
    context = {
        'courses': courses
    }
    return render(request, template_name, context)


# def details(request, pk):
#    # course = Course.objects.get(pk=pk)
#    course = get_object_or_404(Course, pk=pk)
#    template_name = 'courses/details.html'

#    context = {
#        'course': course
#    }

#    return render(request, template_name, context)

def details(request, slug):
    course = get_object_or_404(Course, slug=slug)
    template_name = 'courses/details.html'
    context = dict(course=course)
    return render(request, template_name, context)
