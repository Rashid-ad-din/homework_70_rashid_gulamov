from django.core.exceptions import ValidationError
from django.core.validators import BaseValidator
from django.db import models
from django.db.models import QuerySet

from webapp.managers import TaskManager


def unique(string):
    if len(string) < 2:
        raise ValidationError('Значение не может быть менее 2 символов')
    for i in string:
        if i in '~!@#$%^&*(){}[]?"\',.|/':
            raise ValidationError('Значение не должно содрежать спецсимволы ~!@#$%^&*(){}[]?"\',.|/')


class CustomValidator(BaseValidator):
    def __init__(self, limit_value=2):
        message = 'Значение не может состоять из более чем двух слов. Сейчас %(show_value)s'
        super(CustomValidator, self).__init__(limit_value=limit_value, message=message)

    def compare(self, counter, limit_value):
        return limit_value < counter

    def clean(self, value):
        counter = 0
        for i in value.split(' '):
            counter += 1
        return counter


class Task(models.Model):
    summary = models.CharField(verbose_name="Заголовок задачи",
                               null=False,
                               blank=False,
                               max_length=150,
                               validators=[
                                   unique,
                                   CustomValidator()
                               ])
    description = models.TextField(verbose_name="Полное описание", null=True, blank=True, max_length=2000)
    state = models.ManyToManyField(
        to='webapp.State',
        related_name='states',
        verbose_name='Статус',
        blank=False,
    )
    type = models.ManyToManyField(
        to='webapp.Type',
        related_name='types',
        verbose_name='Тип',
        blank=False
    )
    created_at = models.DateTimeField(verbose_name='Дата изменения', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Дата удаления', auto_now=True)
    project = models.ForeignKey(
        to='webapp.Project',
        verbose_name='Проект',
        related_name='tasks',
        on_delete=models.CASCADE,
    )

    objects = TaskManager()

    def __str__(self):
        return f'Заголовок: {self.summary}, Статус: {self.state.first()}, Тип: {self.type.first()}, Дата обновления:' \
               f' {self.updated_at}'


    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'
