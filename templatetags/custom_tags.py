from django import template
from crime.models import Visitor

register = template.Library()

@register.simple_tag(name="visitor_count")
def visitor_count_tag():
    return Visitor.objects.count()
