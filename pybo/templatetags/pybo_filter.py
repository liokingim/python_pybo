from django import template

register = template.Library()

# 빼기 필터
@register.filter
def sub(value, arg):
    return value - arg