import hashlib
import random
from django.conf import settings
from django.core.mail import send_mail

from django.db import models

from wagtail.core.models import Page

recipient_list = ['ilja.sonin2018@yandex.ru']


class ReviewManager(models.Manager):
    
    def create_obj(self, name, age, review):
        salt = hashlib.sha256(str(random.random()).encode('utf-8') + settings.SECRET_KEY.encode('utf-8')).hexdigest()
        token = hashlib.sha1(salt.encode('utf-8') + name.encode('utf-8')).hexdigest()
        
        url = "https://orlan-chehov.ru/reviews/form/submit?token={}".format(token)

        subject = "Новый отзыв"
        message = "Пришел новый отзыв: \nИмя: {}\nВозраст: {}\nОтзыв: {}\n\nЧтобы выложить отзыв на сайт перейдите по ссылке: \n{}".format(name, age, review, url)
        send_mail(subject, message, settings.EMAIL_HOST_USER, recipient_list)

        review_model = self.create(
            name=name,
            age=age,
            review=review,
            token=token
        )

        return review_model

    def confirm(self, token):
        review = self.get(token=token)
        review.is_active = True
        review.save()
        
        return review

class Reviews(models.Model):

    name = models.CharField("Имя", max_length=100, default="Name")
    age = models.IntegerField("Сколько вам лет", default=1)
    review = models.TextField("Отзыв", default="Review")

    is_active = models.BooleanField("Он валидный", default=False)

    token = models.CharField(max_length=40, default="Token")

    objects = ReviewManager()

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