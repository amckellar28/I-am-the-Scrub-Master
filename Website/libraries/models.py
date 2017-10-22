from django.db import models


class Library(models.Model):
    title = models.CharField(max_length = 140)
    address = models.TextField()
    number = models.CharField(max_length = 140)
    emailaddress = models.EmailField(max_length=254)
    image = models.ImageField(null = True,  blank = True,
                              width_field = "width_field", height_field="height_field")
    height_field = models.IntegerField(default = 0)
    width_field = models.IntegerField(default = 0)
    home_page = models.URLField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title
    def getImage(self):
        if self.image:
            return self.image.url
        if not self.image:
            return '/media/default-placeholder-300x300.png'

class Colleges(models.Model):
    title = models.CharField(max_length = 140)
    rank = models.CharField(max_length = 140)
    address = models.TextField()
    departments = models.TextField()
    emailaddress = models.EmailField(max_length=254)
    image = models.ImageField(null = True,  blank = True,
                              width_field = "width_field", height_field="height_field")
    height_field = models.IntegerField(default = 0)
    width_field = models.IntegerField(default = 0)
    home_page = models.URLField(max_length=200)
    description = models.TextField()


    def __str__(self):
        return self.title
    def getImage(self):
        if self.image:
            return self.image.url
        if not self.image:
            return '/media/default-placeholder-300x300.png'

class Industries(models.Model):
    title = models.CharField(max_length = 140)
    address = models.TextField()
    industrytype = models.TextField()
    emailaddress = models.EmailField(max_length=254)
    image = models.ImageField(null = True,  blank = True,
                              width_field = "width_field", height_field="height_field")
    height_field = models.IntegerField(default = 0)
    width_field = models.IntegerField(default = 0)
    home_page = models.URLField(max_length=200)
    description = models.TextField()
    def getImage(self):
        if self.image:
            return self.image.url
        if not self.image:
            return '/media/default-placeholder-300x300.png'
    def __str__(self):
        return self.title

class Hotels(models.Model):
    title = models.CharField(max_length = 140)
    address = models.TextField()
    number = models.CharField(max_length = 140)
    emailaddress = models.EmailField(max_length=254)
    image = models.ImageField(null = True,  blank = True,
                              width_field = "width_field", height_field="height_field")
    height_field = models.IntegerField(default = 0)
    width_field = models.IntegerField(default = 0)
    home_page = models.URLField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title
    def getImage(self):
        if self.image:
            return self.image.url
        if not self.image:
            return '/media/default-placeholder-300x300.png'

class Parks(models.Model):
    title = models.CharField(max_length = 140)
    address = models.TextField()
    number = models.CharField(max_length = 140)
    emailaddress = models.EmailField(max_length=254)
    image = models.ImageField(null = True,  blank = True,
                              width_field = "width_field", height_field="height_field")
    height_field = models.IntegerField(default = 0)
    width_field = models.IntegerField(default = 0)
    home_page = models.URLField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title
    def getImage(self):
        if self.image:
            return self.image.url
        if not self.image:
            return '/media/default-placeholder-300x300.png'

class Zoos(models.Model):
    title = models.CharField(max_length = 140)
    address = models.TextField()
    number = models.CharField(max_length = 140)
    emailaddress = models.EmailField(max_length=254)
    image = models.ImageField(null = True,  blank = True,
                              width_field = "width_field", height_field="height_field")
    height_field = models.IntegerField(default = 0)
    width_field = models.IntegerField(default = 0)
    home_page = models.URLField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title
    def getImage(self):
        if self.image:
            return self.image.url
        if not self.image:
            return '/media/default-placeholder-300x300.png'

class Museums(models.Model):
    title = models.CharField(max_length = 140)
    address = models.TextField()
    number = models.CharField(max_length = 140)
    emailaddress = models.EmailField(max_length=254)
    image = models.ImageField(null = True,  blank = True,
                              width_field = "width_field", height_field="height_field")
    height_field = models.IntegerField(default = 0)
    width_field = models.IntegerField(default = 0)
    home_page = models.URLField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title
    def getImage(self):
        if self.image:
            return self.image.url
        if not self.image:
            return '/media/default-placeholder-300x300.png'

class Restaurants(models.Model):
    title = models.CharField(max_length = 140)
    address = models.TextField()
    number = models.CharField(max_length = 140)
    emailaddress = models.EmailField(max_length=254)
    image = models.ImageField(null = True,  blank = True,
                              width_field = "width_field", height_field="height_field")
    height_field = models.IntegerField(default = 0)
    width_field = models.IntegerField(default = 0)
    home_page = models.URLField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title
    def getImage(self):
        if self.image:
            return self.image.url
        if not self.image:
            return '/media/default-placeholder-300x300.png'

class Malls(models.Model):
    title = models.CharField(max_length = 140)
    address = models.TextField()
    number = models.CharField(max_length = 140)
    emailaddress = models.EmailField(max_length=254)
    image = models.ImageField(null = True,  blank = True,
                              width_field = "width_field", height_field="height_field")
    height_field = models.IntegerField(default = 0)
    width_field = models.IntegerField(default = 0)
    home_page = models.URLField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title
    def getImage(self):
        if self.image:
            return self.image.url
        if not self.image:
            return '/media/default-placeholder-300x300.png'

class maps(models.Model):
    title = models.CharField(max_length = 140)
    image = models.ImageField(null = True,  blank = True,
                              width_field = "width_field", height_field="height_field")
    height_field = models.IntegerField(default = 0)
    width_field = models.IntegerField(default = 0)
    
    def __str__(self):
        return self.title
    


    
