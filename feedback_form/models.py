from django.db import models

# Create your models here.

class feedback_response(models.Model):
    name = models.CharField(max_length = 60)
    email_id = models.CharField(max_length = 60)
    rating = models.CharField(max_length = 1)
    comment = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
