from django import template
from ..models import Venue
register =template.Library()
@register.simple_tag
def get_recent_venues():

    return Venue.objects.all().order_by('-created_date')[:5]