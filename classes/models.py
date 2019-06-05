from django.db import models

from wagtail.core.models import Page, Orderable
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel
from wagtail.images.edit_handlers import ImageChooserPanel

from modelcluster.fields import ParentalKey

class ClassesPage(Page):
    show_in_menus_default = True
    
    image_classes = models.ForeignKey('wagtailimages.Image',
                                      verbose_name="Картинка для 'Занятия в школе'",
                                      null=True,
                                      blank=True,
                                      on_delete=models.SET_NULL,
                                      related_name='+')
    title_classes = models.CharField("Заголовок 'Занятия в школе'", 
                                     max_length=50,
                                     default="Занятия в школе")
    description_classes = RichTextField("Описание под заголовоком", default="Text")
    time_classes_title = models.CharField("Заголовок 'Расписание занятий'", max_length=50,
                                          default="Расписание занятий")
    time_classes_description = RichTextField("Описание под 'расписание занятий'",
                                             default="Text")

    title_reviews = models.CharField("Заголвок селекции отзывы", 
                                     max_length=50,
                                     default="Что говорят о нас")
    description = RichTextField('Текст под селекции отзывы', default="Text")

    class Meta:
        verbose_name = "Добавить страницу Занятия (не трогать)"
    
    content_panels = Page.content_panels + [
        ImageChooserPanel('image_classes'),
        FieldPanel('title_classes'),
        FieldPanel('description_classes'),
        FieldPanel('time_classes_title'),
        FieldPanel('time_classes_description'),
        InlinePanel('onegroup_users', label="группу обучения. Можно оставить пустым"),
        FieldPanel('title_reviews'),
        FieldPanel('description'),
        InlinePanel('reviews', label="комментарий")
    ]


class OneGroup(Orderable):
    page = ParentalKey(ClassesPage, related_name="onegroup_users")

    image =  models.ForeignKey('wagtailimages.Image',
                                verbose_name="Картинка группы (иконка)",
                                null=True,
                                blank=True,
                                on_delete=models.SET_NULL,
                                related_name='+')
    title = models.CharField("Заголовок", max_length=50, default="Первая группа")
    description = RichTextField('Описание', default="Text")

    panels = [
        ImageChooserPanel('image'),
        FieldPanel('title'),
        FieldPanel('description')
    ]

class Reviews(Orderable):
    page = ParentalKey(ClassesPage, related_name="reviews")

    image =  models.ForeignKey('wagtailimages.Image',
                                verbose_name="Картинка человека",
                                null=True,
                                blank=True,
                                on_delete=models.SET_NULL,
                                related_name='+')
    title = models.CharField("Имя человка", max_length=50, default="Имя человка")
    description = RichTextField('Отзыв', default="Text")

    panels = [
        ImageChooserPanel('image'),
        FieldPanel('title'),
        FieldPanel('description')
    ]