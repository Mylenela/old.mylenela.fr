from django.contrib import admin
from mylenela.projects.models import Category
from mylenela.projects.models import Project


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name_en',)}


class ProjectAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name_en',)}

admin.site.register(Category, CategoryAdmin)
admin.site.register(Project, ProjectAdmin)
