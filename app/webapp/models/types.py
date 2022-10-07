from django.db import models


class Type(models.Model):
    models.ForeignKey(
        to='webapp.Task',
        verbose_name='Тип',
        related_name='types',
        on_delete=models.RESTRICT
    )
    name = models.CharField(verbose_name="Тип", null=False, blank=False, max_length=100)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Тип'
        verbose_name_plural = 'Типы'
