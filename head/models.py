from django.db import models

from wagtail.admin.edit_handlers import FieldPanel
from wagtail.snippets.models import register_snippet

@register_snippet
class Header(models.Model):
    phone = models.CharField("Номер телефона", max_length=50, default="text")
    email = models.EmailField("Почта", max_length=254, default="text")
    
    # Добавить иконки соц сетей

    panels = [
        FieldPanel('phone'),
        FieldPanel('email')
    ]