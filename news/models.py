from django.db import models

from wagtail.core.models import Page

from article.models import ArticlePage

class NewsPage(Page):

    class Meta:
        verbose_name = "Добавить новую страницу новостей (Не трогать!)"
    
    def get_context(self, request):
        context = super().get_context(request)
        context['article'] = ArticlePage.objects.child_of(self).live()
        return context