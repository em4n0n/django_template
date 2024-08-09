from django.db import models
from datetime import datetime

# Create your models here.

class Picture(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_on = models.DateTimeField(default=datetime.now)
    image = models.ImageField(upload_to="images/%Y/%m/%d")

    def __str__(self):
        return self.title
