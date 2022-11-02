from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'basic_App/index.html')

def other(request):
    return render(request, 'basic_App/other.html')

def relative(request):
    return render(request, 'basic_App/relative_url_templates.html')
