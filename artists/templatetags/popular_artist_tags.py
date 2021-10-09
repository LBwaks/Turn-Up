from django import template
from ..models import Artist
register = template.Library()

@register.simple_tag
def get_popular_artists():
    return Artist.objects.order_by('-artist_view')[:5]