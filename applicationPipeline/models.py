from django.db import models

class Application(models.Model):
    STATUS_CHOICES = [
        ("applied", "Applied"),
        ("screening", "Screening"),
        ("interview", "Interview"),
        ("offer", "Offer"),
        ("rejected", "Rejected"),
    ]

    job_title = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="applied"
    )