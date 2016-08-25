from django import template
register = template.Library()


@register.filter(name='times')
def times(number):
    return reversed(range(1, number))
