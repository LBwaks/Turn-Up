from django import template
from artists.models import Category 
from django.db.models import Count
register = template.Library()

@register.simple_tag
def get_all_artist_categories():
    return Category.objects.all().annotate(artists_count=Count('artist'))  