from django.db import models
from django import template

from wagtail.core.models import Page, Orderable
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.snippets.models import register_snippet
from wagtail.core.fields import RichTextField

from modelcluster.fields import ParentalKey
from gallery.models import GalleryPage


class HomePage(Page):
    description = models.CharField("Описание баннера", 
                                   max_length=200, 
                                   help_text="Описание большого баннера, с фотографией", 
                                   default='Текст описание')
    button_title = models.CharField("Текст кнопки на баннере", 
                                    max_length=200, 
                                    default='Записаться к нам')
    mini_about_image = models.ForeignKey('wagtailimages.Image',
                                      verbose_name='Картинка для селекции о нас',
                                      null=True,
                                      blank=True,
                                      on_delete=models.SET_NULL,
                                      related_name='+',
                                      help_text="Изображение должно быть в разрешении 554 на 418")
    mini_about_title = models.CharField("Заголовок для селекции о нас", 
                                        help_text="Заголовок для селекции о нас, который под баннером", 
                                        max_length=200,
                                        default="Заголовок")
    mini_about_description = RichTextField("Описание для селекции о нас",
                                           help_text="Введите описание в селекции о нас",
                                           default="Описание")
    mini_about_button_text = models.CharField("Введите текст кнопки в селекции о нас", 
                                              max_length=200,
                                              default="Узнать подробней")
    feature_title_text = models.CharField("Заголовок для преймуществ",
                                          help_text="Введите заголовлок по умолчанию наши преймущества", 
                                          max_length=200,
                                          default="Заголовок")
    feature_mini_description = RichTextField("Описание преймуществ",
                                            help_text="Введите небольшое описание для преймуществ",
                                            default="Описание")
    gallery_title = models.CharField("Название селекции фотогаллерея", 
                                     max_length=200,
                                     default="Фотогаллерея")
    gallery_description = RichTextField('Описание селекции фотогаллерея', default="Описание")
    what_they_say_about_us_title = models.CharField("Селекция 'что говорят о нас' заголовок", 
                                                    max_length=200, default="Заголовок селекции")
    what_they_say_about_us_description = RichTextField("Селекция 'что говорят о нас' описание", default="Описание")
    first_feedback_image = models.ForeignKey('wagtailimages.Image',
                                      verbose_name='Изображение первого человека, который оставил отзыв',
                                      null=True,
                                      blank=True,
                                      on_delete=models.SET_NULL,
                                      related_name='+',
                                      help_text="Изображение должно быть в разрешении 102 на 104")
    first_feedback_name = models.CharField("Имя первого человека который оставил отзыв", 
                                          max_length=200,
                                          default="Имя")
    first_feedback_description = RichTextField('Текст отзыва, от первого человека', default="Описание")
    second_feedback_image = models.ForeignKey('wagtailimages.Image',
                                      verbose_name='Изображение второго человека, который оставил отзыв',
                                      null=True,
                                      blank=True,
                                      on_delete=models.SET_NULL,
                                      related_name='+',
                                      help_text="Изображение должно быть в разрешении 102 на 104")
    second_feedback_name = models.CharField("Имя второго человека который оставил отзыв", 
                                            max_length=200,
                                            default="Имя")
    second_feedback_description = RichTextField('Текст отзыва, от второго человека', default="Описание")

    content_panels = [
        FieldPanel('title'),
        FieldPanel('description'),
        FieldPanel('button_title'),
        ImageChooserPanel('mini_about_image'),
        FieldPanel('mini_about_title'),
        FieldPanel('mini_about_description'),
        FieldPanel('mini_about_button_text'),
        FieldPanel('feature_title_text'),
        FieldPanel('feature_mini_description'),
        InlinePanel('featured', label="преймущество."),
        FieldPanel('gallery_title'),
        FieldPanel('gallery_description'),
        FieldPanel('what_they_say_about_us_title'),
        FieldPanel('what_they_say_about_us_description'),
        FieldPanel('first_feedback_name'),
        ImageChooserPanel('first_feedback_image'),
        FieldPanel('first_feedback_description'),
        FieldPanel('second_feedback_name'),
        ImageChooserPanel('second_feedback_image'),
        FieldPanel('second_feedback_description'),
    ]

    show_in_menus_default = True

    def get_context(self, request):
        context = super().get_context(request)
        context['gallery'] = GalleryPage.objects.child_of(self).live()[:6]
        return context

    def __str__(self):
        return "Главная"

    class Meta:
        verbose_name = "Добавить домашнюю страницу (Не трогать!)"


class Featured(Orderable):
    page = ParentalKey(HomePage, related_name="featured")
    image = models.ForeignKey('wagtailimages.Image',
                              verbose_name='Картинка преймущества',
                              null=True,
                              blank=True,
                              on_delete=models.SET_NULL,
                              related_name='+',
                              help_text="Изображение должно быть в размером 77 на 77")
    title = models.CharField("Заголовок преймущества", max_length=200, default="Заголовок")
    description = RichTextField("Описание преймущества", default="Описание")

    panels = [
        ImageChooserPanel('image'),
        FieldPanel('title'),
        FieldPanel('description')
    ]