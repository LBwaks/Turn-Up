from django import template
from ..models import Venue,Category

register=template.Library()

@register.simple_tag

def get_related_venue_by_tags(self):
    return Venue.objects.filter(category_slug=self.category_slug).exclude(slug=self.slug)