from django.db import models


class Task(models.Model):
    summary = models.CharField(verbose_name="Заголовок", null=False, blank=False, max_length=150)
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

    def __str__(self):
        return f'Заголовок: {self.summary}, Статус: {self.state}, Тип: {self.type}, Дата обновления: {self.updated_at}'

    def get_state(self, obj):
        return "\n".join([s.name for s in obj.state.all()])

    def get_type(self, obj):
        return "\n".join([t.name for t in obj.type.all()])

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'
