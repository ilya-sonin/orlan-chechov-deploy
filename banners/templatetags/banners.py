from django import template

from head.models import Header

register = template.Library()

@register.inclusion_tag('banners/banners.html', takes_context=True)
def banners(context):
    return {
        'headers_info': Header.objects.all(),
    }