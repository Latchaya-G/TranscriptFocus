# your_app/templatetags/custom_filters.py

from django import template

register = template.Library()

@register.filter(name='time_format')
def time_format(value):
    hours, remainder = divmod(value, 3600)
    minutes, seconds = divmod(remainder, 60)
    return "{:02}:{:02}:{:02}".format(int(hours), int(minutes), int(seconds))
