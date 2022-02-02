from django.shortcuts import render

# Create your views here.

def courses(request):
    template_name = 'courses/index.html'
    return render(request, template_name)
