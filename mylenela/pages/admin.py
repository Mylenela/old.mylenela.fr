from django.contrib import admin
from mylenela.pages.models import Page


class PageAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name_en',)}

admin.site.register(Page, PageAdmin)
