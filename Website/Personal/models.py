from django.db import models

# Create your models here.
class Event(models.Model):
    title = models.CharField(max_length = 140)
    description = models.TextField()
    dates = models.CharField(max_length = 140)
    image = models.ImageField(null = True,  blank = True,
                              width_field = "width_field", height_field="height_field")
    height_field = models.IntegerField(default = 0)
    width_field = models.IntegerField(default = 0)
    home_page = models.URLField(max_length=200)

    def __str__(self):
        return self.title
    def getImage(self):
        if self.image:
            return self.image.url
        if not self.image:
            return '/media/default-placeholder-300x300.png'
        
