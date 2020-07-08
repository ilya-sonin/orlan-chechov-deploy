import datetime

from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.embeds.blocks import EmbedBlock

class ArticlePage(Page):
    preview_text = RichTextField("Превью текст",
                                    help_text="Сокращенное содержание статьи\n" \
                                                "Текст который отображается на главной странице",
                                    default="text")
    date = models.DateField("Дата поста", default=datetime.date.today)
    body = RichTextField("Текст статьи", help_text="Пишите текст статьи", default="text")
    
    content_panels = [
        FieldPanel('title'),
        FieldPanel('preview_text'),
        FieldPanel('body'),
        FieldPanel('date'),
    ]
    
    class Meta:
        verbose_name = "Добавить новую статью (Добавлять как дочернюю страницу к страницы с новостями)"
