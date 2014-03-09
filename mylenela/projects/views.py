# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Project


def view_project(request, slug):
    project = get_object_or_404(Project, slug=slug)

    return render(
        request,
        'project.html',
        {'project': project})
