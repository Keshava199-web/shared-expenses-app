from django.db import models
from django.contrib.auth.models import User


class Settlement(models.Model):
    payer = models.ForeignKey(
        User,
        related_name="payments_made",
        on_delete=models.CASCADE
    )

    receiver = models.ForeignKey(
        User,
        related_name="payments_received",
        on_delete=models.CASCADE
    )

    amount = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )

    settlement_date = models.DateField()

    notes = models.TextField(
        blank=True,
        null=True
    )

    def __str__(self):
        return f"{self.payer} -> {self.receiver} : {self.amount}"