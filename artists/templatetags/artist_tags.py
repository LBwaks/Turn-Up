from django import template
from ..models import Artist

register = template.Library()
@register.simple_tag
def get_recent_artists():
 return Artist.objects.all().order_by('-created_date')[:5]

# def get_categories():
#     return Category.objects.all()
 