import uuid
from django.db import models
from django.contrib.auth.models import User

class Invoices(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    client_name = models.CharField(max_length=30)
    client_email = models.CharField(max_length=30)
    project_name = models.CharField(max_length=30)
    amount = models.IntegerField()
    status = models.BooleanField(default=True)
    link = models.URLField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)