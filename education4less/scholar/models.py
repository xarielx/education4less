from django.db import models
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.


class Scholar(models.Model):
    scholarship_name = models.TextField(default="empty")
    scholarship_link = models.URLField(default="empty")
    award_amount = models.TextField(default="empty")
    geographic_requisite = models.TextField(default="empty")
    enrollment_requisite = models.TextField(default="empty")
    major_requisite = models.TextField(default="empty")
    description = models.TextField(default="empty")
    requirements = models.TextField(default="empty")

    def __str__(self):
        return self.scholarship_name
