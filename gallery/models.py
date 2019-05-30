from django.db import models

from wagtail.core.models import Page, Orderable
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel
from wagtail.core.fields import RichTextField

from modelcluster.fields import ParentalKey


class GalleryPage(Page):

    show_in_menus_default = True

    title_page_h1 = models.CharField("H1 заголовок на странице", max_length=50, default="Заголовок")

    content_panels = Page.content_panels + [
        FieldPanel('title_page_h1'),
        InlinePanel('gallery_images', label="фотографию"),
    ]
    
    class Meta:
        verbose_name = "Добавить страницу фотогаллерии (не трогать!)"


class OneGalleryPage(Orderable):
    page = ParentalKey(GalleryPage, related_name='gallery_images')

    image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.CASCADE, related_name='+'
    )

    panels = [
        ImageChooserPanel('image'),
    ]