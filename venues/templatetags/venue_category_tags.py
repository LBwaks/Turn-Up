from django import template
from venues.models import Category, Venue
from django.db.models import Count

register =template.Library()

@register.simple_tag
def get_all_categories():
    return Category.objects.all().annotate(venues_count=Count('venue_category'))

