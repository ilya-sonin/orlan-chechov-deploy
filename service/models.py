from django.db import models

from wagtail.core.models import Page, Orderable
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel
from wagtail.core.fields import RichTextField
from wagtail.images.edit_handlers import ImageChooserPanel

from modelcluster.fields import ParentalKey

class OneService(Page):
    img_description = models.ForeignKey('wagtailimages.Image',
                                        verbose_name='Картинка для категории',
                                        null=True,
                                        blank=True,
                                        on_delete=models.SET_NULL,
                                        related_name='+')
    description_title = models.CharField("Заголовок описания услуги", 
                                         max_length=50,
                                         default="Подготовка водителей категории «В»")
    description_text = RichTextField("Описание услуги", default="Описание")

    title_learning_information = models.CharField("Заголовок сведение обучения", max_length=50,
                                                  default="Сведения об обучении")

    title_price = models.CharField("СТОИМОСТЬ ОБУЧЕНИЯ", max_length=50, default="СТОИМОСТЬ ОБУЧЕНИЯ")
    description_price = RichTextField("Описание", default="Описание")

    title_date = models.CharField("СРОК ОБУЧЕНИЯ", max_length=50, default="СРОК ОБУЧЕНИЯ")
    description_date = RichTextField("Описание", default="Описание")

    title_age = models.CharField("НЕОБХОДИМЫЙ ВОЗРАСТ", max_length=50, default="НЕОБХОДИМЫЙ ВОЗРАСТ")
    description_age = RichTextField("Описание", default="Описание")

    content_panels = Page.content_panels + [
        ImageChooserPanel('img_description'),
        FieldPanel('description_title'),
        FieldPanel('description_text'),
        FieldPanel('title_learning_information'),
        FieldPanel('title_price'),
        FieldPanel('description_price'),
        FieldPanel('title_date'),
        FieldPanel('description_date'),
        FieldPanel('title_age'),
        FieldPanel('description_age'),
    ]
    
    class Meta:
        verbose_name = "Добавить услугу"


class ServicePage(Page):
    show_in_menus_default = True

    selection_title = models.CharField("Текст перечень услуг", max_length=50, default="Перечень услуг")
    selection_description = RichTextField("Описание перечня услуг", default="Описание")

    content_panels = Page.content_panels + [
        FieldPanel('selection_title'),
        FieldPanel('selection_description')
    ]

    def get_context(self, request):
        context = super().get_context(request)
        context['services'] = OneService.objects.child_of(self).live()
        return context

    class Meta:
        verbose_name = "страницу со всеми услугами (не трогать!)"
