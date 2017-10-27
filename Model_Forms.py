from django.db import models

class Event_case(models.Model):
    <fieldset>
    # Creating forms/ charfields for the length of 100 chars that can be inputted
    Header = models.CharField(max_length = 100);
    description = models.Textfield()
    dates - models.CharField(max_length = 100);

    # Collecting the height and width of the image
    Photo_Profile = models.Imagefield (null = True,  blank = True,
                              width = "width_field", height="height_field")
    height = models.IntegerField(default = 0)
    width = models.IntegerField(default = 0)
    home_page = models.URLField(max_length=200)

    # Field sets are to put all these forms within 1 field box
    </fieldset>
    def __str__(self):
        return self.title
    def getImage(self):
        if self.image:
            return self.image.url
        if not self.image:
            return '/media/default-placeholder-300x300.png'


class Map_Case(models.Model):
# This code is to create a form for the Map
    <fieldset>
#First you need to make Charfields/ Text boxes where both the Area name
# And longitude and latitude can be implemented and stored

    Map_Area = models.CharField(max_length = 100)
    Latitude = models.CharField(max_length = 100)
    Longitude = models.CharField(max_length = 100)
    Area_description = models.TextField()

# Collecting the height of the map image

    Map_Profile = models.Imagefield (null = True,  blank = True,
                              width = "width_field", height="height_field")
    height = models.IntegerField(default = 0)
    width = models.IntegerField(default = 0)
    </fieldset>
# Returning strings, the title, and image that was placed into the field

        def __str__(self):
        return self.title
    def getImage(self):
        if self.image:
            return self.image.url
        if not self.image:
            return '/media/default-placeholder-600x600.png'
#making the map 600x 600 to increase visibility in the platform
