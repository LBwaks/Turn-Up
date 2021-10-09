from django import template
from blogs.models import Category
from django.db.models import Count

register=template.Library()
@register.simple_tag
def get_all_categories():
    return Category.objects.all().annotate(category_count=Count('name'))