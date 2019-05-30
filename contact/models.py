from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel

class ContactPage(Page):
    geo_description = RichTextField("Адрес огранизации", default="Text")
    phone = RichTextField("Номер телефона", default="Text")
    email = RichTextField('Введите почту', default="Text")

    content_panels = Page.content_panels + [
        FieldPanel('geo_description'),
        FieldPanel('phone'),
        FieldPanel('email')
    ]

    class Meta:
        verbose_name = "Добавить страницу контактов (не трогать)"