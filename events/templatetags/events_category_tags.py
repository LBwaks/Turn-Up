from django import template
from events.models import Category
from django.db.models import Count
register=template.Library()
@register.simple_tag
def get_all_events_categories():
    return Category.objects.all().annotate(events_count=Count('event_category'))


