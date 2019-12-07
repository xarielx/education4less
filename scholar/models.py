from django.db import models
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.


class Scholar(models.Model):
    scholarship_name = models.TextField(default="empty", blank=True, null=True)
    scholarship_link = models.TextField(default="empty", blank=True, null=True)
    award_amount = models.TextField(default="empty", blank=True, null=True)
    geographic_requisite = models.TextField(
        default="empty", blank=True, null=True)
    enrollment_requisite = models.TextField(
        default="empty", blank=True, null=True)
    major_requisite = models.TextField(default="empty", blank=True, null=True)
    description = models.TextField(default="empty", blank=True, null=True)
    requirements = models.TextField(default="empty", blank=True, null=True)

    class Meta:
        ordering = ["id"]

    def __str__(self):
        return f"{self.scholarship_name}"
