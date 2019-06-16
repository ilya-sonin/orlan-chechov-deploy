from django.db import models

from wagtail.core.models import Page, Orderable

from wagtail.core.fields import RichTextField, StreamField
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel

from wagtail.core import blocks
from wagtail.documents.blocks import DocumentChooserBlock
from wagtail.images.blocks import ImageChooserBlock


class AboutDocsOrlan(Page):

    date_of_creation = RichTextField('Дата создания тектс', default="Default")
    brief_information = RichTextField('Информация об учреждении', default="Default")
    founder = RichTextField('Учредитель', default="Default")
    locate = RichTextField('Местонахождение', default="Default")
    driving_schedule = RichTextField('График вождения', default="Default")
    schedule = RichTextField('График работы', default="Default")
    numbers = RichTextField('Контактные телефоны', default="Default")
    email = RichTextField('Email', default="Default")

    class Meta:
        verbose_name = "Об автошколе"

    content_panels = Page.content_panels + [
        FieldPanel('date_of_creation'),
        FieldPanel('brief_information'),
        FieldPanel('founder'),
        FieldPanel('locate'),
        FieldPanel ('driving_schedule'),
        FieldPanel('schedule'),
        FieldPanel('numbers'),
        FieldPanel('email'),
    ]


class ChildAboutPage(Page):
    
    body = StreamField([
        ('h1', blocks.CharBlock(classname="h1 заголовок")),
        ('h2', blocks.CharBlock(classname="h2 заголовок")),
        ('h3', blocks.CharBlock(classname="h3 заголовок")),
        ('h4', blocks.CharBlock(classname="h4 заголовок")),
        ('h5', blocks.CharBlock(classname="h5 заголовок")),
        ('Текст', blocks.RichTextBlock()),
    ], default=None, verbose_name="Обычный текст")

    bl_ones = StreamField([
        ('ДокументPDF', DocumentChooserBlock(classname="документ pdf")),
        ('мб_с_описанием', blocks.ListBlock(blocks.StructBlock([
            ('icon', ImageChooserBlock(classname="иконка")),
            ('title', blocks.CharBlock(classname="заголовок для блока")),
            ('description', blocks.RichTextBlock())
        ]))),
        ('мб', blocks.ListBlock(blocks.StructBlock([
            ('icon', ImageChooserBlock(classname="иконка")),
            ('title', blocks.CharBlock(classname="заголовок для блока")),
        ]))),
    ], default=None, verbose_name="Одинарный блок")

    bl_many = StreamField([
        ('ДокументPDF', DocumentChooserBlock(classname="документ pdf")),
        ('мб_с_описанием', blocks.ListBlock(blocks.StructBlock([
            ('icon', ImageChooserBlock(classname="иконка")),
            ('title', blocks.CharBlock(classname="заголовок для блока")),
            ('description', blocks.RichTextBlock())
        ]))),
        ('мб', blocks.ListBlock(blocks.StructBlock([
            ('icon', ImageChooserBlock(classname="иконка")),
            ('title', blocks.CharBlock(classname="заголовок для блока")),
        ]))),    
    ], default=None, verbose_name="Длинный блок")
    
    class Meta:
        verbose_name = "Создать дочернюю страницу об автошколе"

    content_panels = Page.content_panels + [
        StreamFieldPanel('body'),
        StreamFieldPanel('bl_ones'),
        StreamFieldPanel('bl_many'),
    ]