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
    
obj = Picture(title = "Remmington", description = "cat")
obj.save()

# obj = Picture.object.get(id=1)
# obj.title = "Picture"
# obj.save()

# Picture.object.all()