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
    description_learning_information = RichTextField("Описание под заголовком",
                                                     default="Описание")

    content_panels = Page.content_panels + [
        ImageChooserPanel('img_description'),
        FieldPanel('description_title'),
        FieldPanel('description_text'),
        FieldPanel('title_learning_information'),
        FieldPanel('description_learning_information'),
        InlinePanel('learnobj', label="блок информации")
    ]
    
    class Meta:
        verbose_name = "Добавить услугу"


class LearningInformationOneObject(Orderable):
    page = ParentalKey(OneService, related_name="learnobj")
    img = models.ForeignKey('wagtailimages.Image',
                            verbose_name='Картинка блока информации',
                            null=True,
                            blank=True,
                            on_delete=models.SET_NULL,
                            related_name='+')
    title = models.CharField("Заголовок", max_length=50, default="Заголовок")
    description = RichTextField("Описание", default="Описание")

    panels = [
        ImageChooserPanel('img'),
        FieldPanel('title'),
        FieldPanel('description'),
    ]


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
