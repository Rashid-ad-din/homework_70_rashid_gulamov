from django.db import models


class Type(models.Model):
    name = models.CharField(verbose_name="Тип", null=False, blank=False, max_length=100)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Тип'
        verbose_name_plural = 'Типы'
