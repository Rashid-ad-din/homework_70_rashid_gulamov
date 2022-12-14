from django.db.models import QuerySet, Manager


class TaskManager(Manager):

    def get_queryset(self):
        return QuerySet(self.model, using=self._db).order_by('-updated_at')

    def without_deleted(self):
        return self.get_queryset().exclude(is_deleted=True)
