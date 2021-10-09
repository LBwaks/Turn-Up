from django import template
from ..models import Artist,Category
from django.db.models import Count
register = template.Library()

@register.simple_tag
 
 
def get_related_artist_by_tags(self):
       return Artist.objects.filter(
           category_slug=self.category_slug
        ).exclude(slug=self.slug)