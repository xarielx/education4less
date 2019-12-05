from django.db import models
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.


class Scholar(models.Model):
    scholarship_name = models.TextField(default="empty")
    scholarship_link = models.URLField(default="empty")
    award_amount = models.CharField(max_length=100, default="$0")
    geographic_requisite = models.TextField(default="empty")
    enrollment_requisite = models.TextField(default="empty")
    major_requisite = models.TextField(default="empty")
    description = models.TextField(default="empty")
    requirements = models.TextField(default="empty")

    class Meta:
        ordering = ["award_amount"]

    def __str__(self):
        return f"{self.scholarship_name}"
