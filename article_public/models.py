from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class article(models.Model):
     title = models.CharField(max_length=200, null=True)
     created_by = models.ForeignKey(User, related_name='created_by_user', on_delete=models.CASCADE, null=True)
     description = models.TextField(null=True)
     Creation_date=models.DateTimeField(auto_now_add=True, null=True)
     Is_published=models.BooleanField(default=True, null=True)