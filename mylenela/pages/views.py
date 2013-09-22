# -*- coding: utf-8 -*-
from mylenela.pages.models import Page
from mylenela.projects.models import Project
from mylenela.projects.models import Category
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.core.cache import cache


def view_home(request):
    if not cache.get('page:home'):
        home = get_object_or_404(Page, slug="home")
        cache.set('page:home', home)
    home = cache.get('page:home')

    if not cache.get('categories'):
        categories = Category.objects.all()
        cache.set('categories', categories)
    categories = cache.get('categories')

    if not cache.get('projects'):
        projects = Project.objects.all().order_by('-date')
        cache.set('projects', projects)
    projects = cache.get('projects')

    return render(
        request,
        "home.html",
        {"home": home, "categories": categories, "projects": projects})
