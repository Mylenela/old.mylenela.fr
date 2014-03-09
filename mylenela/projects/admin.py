# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import Image
from .models import Project
from .models import Category


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name_en',)}


class ProjectAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name_en',)}


admin.site.register(Image)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Project, ProjectAdmin)
