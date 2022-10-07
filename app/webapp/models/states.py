from django.db import models


class State(models.Model):
    models.ForeignKey(
        to='webapp.Task',
        verbose_name='Статус',
        related_name='states',
        on_delete=models.RESTRICT
    )
    name = models.CharField(verbose_name="Статус", null=False, blank=False, max_length=100)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'
