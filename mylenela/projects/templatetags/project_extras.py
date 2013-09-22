# -*- coding:utf-8 -*-
from django import template

register = template.Library()


@register.filter('class')
def get_class(obj, prefix):
    return obj.get_class(prefix)
