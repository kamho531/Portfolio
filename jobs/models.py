from django.db import models

# Create your models here.
class Job(models.Model):
    
    # Images
    image = models.ImageField(upload_to='images/')

    # Name
    name = models.CharField(max_length=100)

    # summary
    summary = models.TextField(max_length=800)

    # link
    link = models.URLField(max_length=500)

    def __str__(self):
        return self.name
