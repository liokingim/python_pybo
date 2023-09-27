import markdown
from django import template
from django.utils.safestring import mark_safe

register = template.Library()

# 빼기 필터
@register.filter
def sub(value, arg):
    return value - arg

# markdown
@register.filter
def mark(value):
    extensions = ["ml2br", "fenced_code"]
    return mark_safe(markdown.markdown(value, extensions=extensions))