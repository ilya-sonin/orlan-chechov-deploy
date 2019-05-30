from django.db import models

from wagtail.core.models import Page, Orderable

from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel
from wagtail.images.edit_handlers import ImageChooserPanel
from modelcluster.fields import ParentalKey


class AboutDocsOrlan(Page):
    first_image = models.ForeignKey('wagtailimages.Image',
                                    verbose_name='Первая картинка в селекции основные сведения',
                                    null=True,
                                    blank=True,
                                    on_delete=models.SET_NULL,
                                    related_name='+',
                                    help_text="Изображение должно быть в разрешении ")
    second_image = models.ForeignKey('wagtailimages.Image',
                                      verbose_name='Вторая картинка в селекции основные сведения',
                                      null=True,
                                      blank=True,
                                      on_delete=models.SET_NULL,
                                      related_name='+',
                                      help_text="Изображение должно быть в разрешении ")
    content_panels = Page.content_panels + [
        ImageChooserPanel('first_image'),
        ImageChooserPanel('second_image'),
        InlinePanel('star_info', label="Создание основное сведение"),
    ]

    class Meta:
        verbose_name = "информация об оброзавательной организации (не трогать!)"


class Star_info(Orderable):
    page = ParentalKey(AboutDocsOrlan, related_name="star_info")
    title = models.CharField("Заголовок селекции которую вы хотите описание", 
                             max_length=50,
                             default="Заголовок")
    description = RichTextField("Описание селекции",
                                default="Text")

    panels = [
        FieldPanel('title'),
        FieldPanel('description')
    ]