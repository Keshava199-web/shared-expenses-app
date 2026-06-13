from django.db import models


class ImportJob(models.Model):
    STATUS_CHOICES = [
        ("pending", "Pending"),
        ("completed", "Completed"),
        ("failed", "Failed"),
    ]

    file_name = models.CharField(max_length=255)

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="pending"
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.file_name


class ImportAnomaly(models.Model):
    import_job = models.ForeignKey(
        ImportJob,
        on_delete=models.CASCADE,
        related_name="anomalies"
    )

    row_number = models.IntegerField()

    issue_type = models.CharField(
        max_length=255
    )

    action_taken = models.TextField()

    original_value = models.TextField(
        blank=True,
        null=True
    )

    resolved_value = models.TextField(
        blank=True,
        null=True
    )

    def __str__(self):
        return f"Row {self.row_number} - {self.issue_type}"