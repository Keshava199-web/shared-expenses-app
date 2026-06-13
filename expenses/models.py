from django.db import models
from django.contrib.auth.models import User
from groups.models import Group


class SplitType(models.TextChoices):
    EQUAL = "equal", "Equal"
    EXACT = "exact", "Exact"
    PERCENTAGE = "percentage", "Percentage"
    SHARES = "shares", "Shares"


class Expense(models.Model):
    group = models.ForeignKey(
        Group,
        on_delete=models.CASCADE,
        related_name="expenses"
    )

    title = models.CharField(max_length=255)

    description = models.TextField(
        blank=True,
        null=True
    )

    amount = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )

    currency = models.CharField(
        max_length=10,
        default="INR"
    )

    expense_date = models.DateField()

    paid_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="paid_expenses"
    )

    split_type = models.CharField(
        max_length=20,
        choices=SplitType.choices
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.title} - {self.amount} {self.currency}"


class ExpenseParticipant(models.Model):
    expense = models.ForeignKey(
        Expense,
        on_delete=models.CASCADE,
        related_name="participants"
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    share_amount = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        null=True,
        blank=True
    )

    percentage = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        null=True,
        blank=True
    )

    shares = models.PositiveIntegerField(
        null=True,
        blank=True
    )

    class Meta:
        unique_together = ("expense", "user")

    def __str__(self):
        return f"{self.user.username} - {self.expense.title}"