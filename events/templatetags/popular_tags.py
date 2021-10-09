from django import template
from ..models import Event

register=template.Library()
@register.simple_tag
def get_popular_events():
    return Event.objects.all().order_by('-event_view')[:5]
