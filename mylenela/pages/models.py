# -*- coding: utf-8 -*-
from django.db import models
from transmeta import TransMeta


class Page(models.Model):
    __metaclass__ = TransMeta

    name = models.CharField(max_length=50, verbose_name='Name')
    slug = models.SlugField(max_length=100, unique=True)
    content = models.TextField(verbose_name='Content')

    class Meta:
        translate = ('name', 'content',)

    def __unicode__(self):
        return self.name
