from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# scholarship_name	 scholarship_link	 award_amount	 geographic_requisite	 enrollment_requisite	 major_requisite	 description


class Post(models.Model):
    title = models.CharField(max_length=100, default="empty")
    content = models.TextField(default="empty")
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default="ariel")

    def __str__(self):
        return self.title
