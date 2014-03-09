# -*- coding: utf-8 -*-
from django.shortcuts import get_object_or_404
from django.shortcuts import render

from .models import Page
from ..projects.models import Project
from ..projects.models import Category


def view_home(request):
    home = get_object_or_404(Page, slug="home")
    categories = Category.objects.all()
    projects = Project.objects.all().order_by('-date')

    return render(
        request,
        "home.html",
        {"home": home, "categories": categories, "projects": projects})
