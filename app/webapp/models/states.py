from django.db import models


class State(models.Model):
    name = models.CharField(verbose_name="Статус", null=False, blank=False, max_length=100)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'
