from django import template
from ..models import Venue
from django.db.models import Max,Count

register=template.Library()
@register.simple_tag
def get_popular_venues():
    return Venue.objects.order_by('venue_view')[:5]



