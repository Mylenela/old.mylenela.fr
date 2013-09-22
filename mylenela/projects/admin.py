from django.contrib import admin
from mylenela.projects.models import Image
from mylenela.projects.models import Project
from mylenela.projects.models import Category


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name_en',)}


class ProjectAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name_en',)}


admin.site.register(Image)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Project, ProjectAdmin)
