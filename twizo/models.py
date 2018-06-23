from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Message(models.Model):
    messageID= models.CharField(max_length=255)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        get_latest_by = 'created'
