# -*- coding: utf-8 -*-
from datetime import datetime
from django.db import models
from django.db.models import permalink
from transmeta import TransMeta


class Image(models.Model):
    image = models.FileField(upload_to='images')

    def __unicode__(self):
        return unicode(self.image)


class Category(models.Model):
    __metaclass__ = TransMeta

    name = models.CharField(max_length=50, verbose_name='Name')
    slug = models.SlugField(max_length=100, unique=True)

    class Meta:
        translate = ('name',)
        verbose_name_plural = "Categories"

    def __unicode__(self):
        return self.name


class Project(models.Model):
    __metaclass__ = TransMeta

    name = models.CharField(max_length=50, verbose_name='Name')
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField(verbose_name='Description')
    link = models.URLField(help_text="Project Url", blank=True, null=True)
    date = models.DateField(db_index=True, default=datetime.now)
    categories = models.ManyToManyField(
        Category, help_text="Project categories")
    cover = models.ForeignKey(
        Image, null=True, help_text="Cover image", related_name="cover")
    images = models.ManyToManyField(Image, related_name="images")

    class Meta:
        translate = ('name', 'description',)

    def __unicode__(self):
        return self.name

    def get_images(self):
        return self.images.split(',')

    def get_class(self, prefix):
        r = ""
        categories = self.categories.all()
        for category in categories:
            r += " %s-%s" % (prefix, category.slug)
        return r

    @permalink
    def get_absolute_url(self):
        return ('view_project', None, {'slug': self.slug})
