from django.db import models

from wagtail.core.models import Page

class Reviews(models.Model):

    name = models.CharField("Имя", max_length=100, default="Name")
    age = models.IntegerField("Сколько вам лет", default=1)
    review = models.TextField("Отзыв", default="Review")

    is_active = models.BooleanField("Он активен", default=False)

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"

    def __str__(self):
        return self.name

class ReviewsPage(Page):
    
    def get_context(self, request):
        context = super().get_context(request)
        context['reviews'] = Reviews.objects.all()
        return context
    
    class Meta:
        verbose_name = "Добавить страницу отзывов"