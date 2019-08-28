from django.db import models

from wagtail.core.models import Page

class Reviews(models.Model):

    name = models.CharField("Имя", max_length=100)
    age = models.IntegerField("Сколько вам лет")
    review = models.TextField("Отзыв")

    class Meta:
        verbose_name = "Review"
        verbose_name_plural = "Reviews"

    def __str__(self):
        return self.name

class ReviewsPage(Page):
    
    def get_context(self, request):
        context = super().get_context(request)
        context['reviews'] = Reviews.objects.all()
        return context
    
    class Meta:
        verbose_name = "Добавить страницу отзывов"