# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import Page


class PageAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name_en',)}

admin.site.register(Page, PageAdmin)
