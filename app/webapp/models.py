from django.db import models


class Item(models.Model):
    description = models.CharField(max_length=250, null=False, blank=False, verbose_name='Описание')
    state = models.CharField(max_length=50, null=False, blank=False, default='new', verbose_name='Статус')
    date_to_do = models.DateField(null=True, blank=True, verbose_name='Дата выполнения')

    def __str__(self):
        return f'Описание: {self.description}, Статус: {self.state}, Дата выполнения: {self.date_to_do}'
