from django.shortcuts import render
from .models import Project


# Create your views here.

def home_view_function(request):
    projects = Project.objects.all()
    return render(request, "portfolio_app_templates/home_page_portfolio_app.html", {'projects': projects})