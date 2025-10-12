from django.db import models
from accounts.models import CustomUser
class Notification(models.Model):
    actor = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    recipient = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    verb = models.CharField(max_length=255)
    target = models.GenericForeignKey('content_type', 'object_id')
    timestamp = models.DateTimeField(auto_now_add=True)
# Create your models here.
