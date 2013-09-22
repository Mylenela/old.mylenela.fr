from django.db import models
from transmeta import TransMeta
from django.core.cache import cache


class Page(models.Model):
    __metaclass__ = TransMeta

    name = models.CharField(max_length=50, verbose_name='Name')
    slug = models.SlugField(max_length=100, unique=True)
    content = models.TextField(verbose_name='Content')

    class Meta:
        translate = ('name', 'content',)

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        cache.delete("page:%s" % self.slug)
        cache.set("page:%s" % self.slug, self)
        cache.delete("pages")
        cache.set("pages", Page.objects.all())
        super(Page, self).save(*args, **kwargs)
