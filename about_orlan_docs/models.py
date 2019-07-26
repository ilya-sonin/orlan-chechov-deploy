from django.db import models

from wagtail.core.models import Page, Orderable

from wagtail.core.fields import RichTextField, StreamField
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel

from wagtail.core import blocks
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
        FieldPanel('driving_schedule'),
        FieldPanel('schedule'),
        FieldPanel('numbers'),
        FieldPanel('email'),
    ]


class ChildAboutPage(Page):

    body_mother = StreamField([
        ('child', blocks.StreamBlock([
            ('Текст', blocks.RichTextBlock()),
            ('документ', blocks.ListBlock(blocks.StructBlock([
                ('title', blocks.CharBlock(classname="Заголовок")),
                ('static_name', blocks.CharBlock(classname="ссылка на документ")),
            ]))),
            ('мб_с_описанием', blocks.ListBlock(blocks.StructBlock([
                ('icon', ImageChooserBlock(classname="иконка")),
                ('title', blocks.CharBlock(classname="заголовок для блока")),
                ('description', blocks.RichTextBlock())
            ]))),
            ('мб', blocks.ListBlock(blocks.StructBlock([
                ('icon', ImageChooserBlock(classname="иконка")),
                ('title', blocks.CharBlock(classname="заголовок для блока")),
            ]))),
            ('документ_строка', blocks.ListBlock(blocks.StructBlock([
                ('title', blocks.CharBlock(classname="Заголовок")),
                ('static_name', blocks.CharBlock(classname="ссылка на документ")),
            ]))),
            ('мб_с_описанием_строка', blocks.ListBlock(blocks.StructBlock([
                ('icon', ImageChooserBlock(classname="иконка")),
                ('title', blocks.CharBlock(classname="заголовок для блока")),
                ('description', blocks.RichTextBlock())
            ]))),
            ('мб_строка', blocks.ListBlock(blocks.StructBlock([
                ('icon', ImageChooserBlock(classname="иконка")),
                ('title', blocks.CharBlock(classname="заголовок для блока")),
            ]))),
            ('два_фото', blocks.ListBlock(blocks.StructBlock([
                ('static_name1', blocks.CharBlock(classname="Название первой фото")),
                ('static_name2', blocks.CharBlock(classname="Название второго фото")),
                ('static_name3', blocks.CharBlock(classname="Название третьего фото")),
            ]))),
        ]))
    ], default=None, verbose_name="Большой блок", null=True,blank=True)

    class Meta:
        verbose_name = "Создать дочернюю страницу об автошколе"

    content_panels = Page.content_panels + [
        StreamFieldPanel('body_mother')
    ]