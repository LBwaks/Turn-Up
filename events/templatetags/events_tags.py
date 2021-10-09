from django import template
from ..models import Event

register=template.Library()
@register.simple_tag
def get_recent_events():
    return Event.objects.all().order_by('-created_date')[:5]