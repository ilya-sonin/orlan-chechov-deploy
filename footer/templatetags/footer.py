from django import template
from wagtail.core.models import Page

register = template.Library()

@register.inclusion_tag('footer/footer.html', takes_context=True)
def footer(context):
    contact_data = Page.objects.get(slug="contact")
    return {
        'contact': contact_data.specific,
        'request': context['request'],
    }