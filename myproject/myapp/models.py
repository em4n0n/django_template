from django.db import models

# Create your models here.

class Picture(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title
    
# obj = Picture(title = "Remmington", description = "cat")
# obj.save()

# to modify an object
# obj = Picture.object.get(id=1)
# obj.title = "Picture"
# obj.save()

# Picture.object.all()

# to delete an object
# obj = Picture.object.get(id=1)
# obj.delete()

# Picture.object.all()