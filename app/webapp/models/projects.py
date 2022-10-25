from django.db import models
from django.conf import settings


class Project(models.Model):
    title = models.CharField(verbose_name='Проект', max_length=250, null=False, blank=False)
    description = models.TextField(verbose_name='Описание', max_length=2500, null=True, blank=True)
    date_start = models.DateField(verbose_name='Дата начала', null=False, blank=False)
    date_end = models.DateField(verbose_name='Дата окончания', null=True, blank=True)
    user = models.ManyToManyField(
        to=settings.AUTH_USER_MODEL,
        related_name='projects',
        verbose_name='Пользователь'
    )

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'
