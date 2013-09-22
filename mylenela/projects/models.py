# -*- coding: utf-8 -*-
from datetime import datetime
from django.db import models
from django.db.models import permalink
from django.core.cache import cache
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

    def save(self, *args, **kwargs):
        cache.delete('category:%s' % self.slug)
        cache.set('category:%s' % self.slug, self)
        cache.delete('categories')
        cache.set('categories', Category.objects.all())
        super(Category, self).save(*args, **kwargs)


class Project(models.Model):
    __metaclass__ = TransMeta

    name = models.CharField(max_length=50, verbose_name='Name')
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField(verbose_name='Description')
    link = models.URLField(help_text="Project Url", blank=True, null=True)
    date = models.DateField(db_index=True, default=datetime.now)
    categories = models.ManyToManyField(Category, help_text="Project categories")
    cover = models.ForeignKey(Image, help_text="Cover image", related_name="cover")
    images = models.ManyToManyField(Image, related_name="images")

    class Meta:
        translate = ('name', 'description',)

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        cache.delete('project:%s:categories' % self.slug)
        super(Project, self).save(*args, **kwargs)
        cache.set('project:%s:categories' % self.slug, self.categories.all())

    def get_images(self):
        return self.images.split(',')

    @property
    def get_categories(self):
        if not cache.get('project:%s:categories' % self.slug):
            categories = self.categories.all()
            cache.set('project:%s:categories' % self.slug, categories)
        return cache.get('project:%s:categories' % self.slug)

    def get_class(self, prefix):
        r = ""
        if not cache.get('project:%s:categories' % self.slug):
            categories = self.categories.all()
            cache.set('project:%s:categories' % self.slug, categories)
        categories = cache.get('project:%s:categories' % self.slug)
        for category in categories:
            r += " %s-%s" % (prefix, category.slug)
        return r

    @permalink
    def get_absolute_url(self):
        return ('view_project', None, {'slug': self.slug})
