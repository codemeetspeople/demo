from django.views.generic import TemplateView
from django.shortcuts import get_object_or_404

from blog import models


class IndexView(TemplateView):
    template_name = 'blog/index.tpl'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        categories = models.Category.objects.all()
        context.update({'categories': categories})

        return context


class CategoryView(TemplateView):
    template_name = 'blog/category.tpl'

    def get_context_data(self, category_id, **kwargs):
        context = super().get_context_data(**kwargs)

        category = get_object_or_404(models.Category, pk=category_id)
        context.update({'category': category})

        return context


class ArticleView(TemplateView):
    template_name = 'blog/article.tpl'

    def get_context_data(self, category_id, article_id, **kwargs):
        context = super().get_context_data(**kwargs)

        article = get_object_or_404(models.Article, pk=article_id)
        context.update({'article': article})

        return context
