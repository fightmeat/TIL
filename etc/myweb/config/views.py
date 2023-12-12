from django.shortcuts import render


# Template(템플릿) : *.html, css, javascript....

def home(request):
    return render(request, 'index.html')
