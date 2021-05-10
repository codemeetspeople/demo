from django.db import models
from django.utils.translation import ugettext as _

from tinymce.models import HTMLField


class Category(models.Model):
    class Meta:
        verbose_name = _('Категория')
        verbose_name_plural = _('Категории')

    title = models.CharField(
        verbose_name=_('Название'),
        max_length=255,
        null=False,
        blank=False,
        unique=True
    )

    description = HTMLField(
        verbose_name=_('Описание')
    )

    def __str__(self):
        return self.title


class Article(models.Model):
    class Meta:
        verbose_name = _('Статья')
        verbose_name_plural = _('Статьи')

    title = models.CharField(
        verbose_name=_('Название'),
        max_length=255,
        null=False,
        blank=False
    )

    content = HTMLField(
        verbose_name=_('Контент')
    )

    category = models.ForeignKey(
        to='Category',
        related_name='articles',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        verbose_name=_('Категория')
    )

    def __str__(self):
        return self.title
