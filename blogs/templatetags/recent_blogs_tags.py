from django import template
from ..models import Blog
register=template.Library()
@register.simple_tag
def get_recent_blogs():
    return Blog.objects.all().order_by('-created_date')[:5]