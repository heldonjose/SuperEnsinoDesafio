from django.db import models


class TimeStampableMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        abstract = True
