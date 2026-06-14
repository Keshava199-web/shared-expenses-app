from django.db import models
from django.conf import settings

class Group(models.Model):
    name = models.CharField(max_length=255)

    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.name


class Membership(models.Model):
    group = models.ForeignKey(
        Group,
        on_delete=models.CASCADE
    )

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    joined_at = models.DateField()

    left_at = models.DateField(
        null=True,
        blank=True
    )

    class Meta:
        unique_together = ("group", "user")