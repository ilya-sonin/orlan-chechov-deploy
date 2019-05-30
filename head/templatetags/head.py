from django import template
from head.models import Header
from wagtail.core.models import Page

register = template.Library()

@register.inclusion_tag('head/head.html', takes_context=True)
def head(context):
    homepage = Page.objects.get(slug='home')
    menu = homepage.get_children().live().in_menu()
    return {
        'header': Header.objects.all(),
        'menu': menu,
        'request': context['request'],
    }