# -*- coding: utf-8 -*-
from mylenela.projects.models import Project
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.core.cache import cache


def view_project(request, slug):
    if not cache.get('project:%s' % slug):
        project = get_object_or_404(Project, slug=slug)
        cache.set('project:%s' % slug, project)
    project = cache.get('project:%s' % slug)

    return render(
        request,
        'project.html',
        {'project': project})
