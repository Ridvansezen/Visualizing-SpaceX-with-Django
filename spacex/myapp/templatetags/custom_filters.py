from django import template
from datetime import datetime

register = template.Library()

@register.filter
def date_only_filter(s):
    date_object = datetime.strptime(s, "%Y-%m-%dT%H:%M:%S.%fZ")
    return date_object.date()