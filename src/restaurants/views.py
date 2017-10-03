from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    html_var = 'Daniz'
    html_ = f"""<h1>Hallo {html_var}!</h1>"""
    return HttpResponse(html_)
