from django.db import models


class Library(models.Model):
    title = models.CharField(max_length = 140)
    address = models.TextField()
    number = models.CharField(max_length = 140)
    emailaddress = models.EmailField(max_length=254)

    def __str__(self):
        return self.title

class Colleges(models.Model):
    title = models.CharField(max_length = 140)
    address = models.TextField()
    departments = models.TextField()
    emailaddress = models.EmailField(max_length=254)

    def __str__(self):
        return self.title

class Industries(models.Model):
    title = models.CharField(max_length = 140)
    address = models.TextField()
    industrytype = models.TextField()
    emailaddress = models.EmailField(max_length=254)

    def __str__(self):
        return self.title

class Hotels(models.Model):
    title = models.CharField(max_length = 140)
    address = models.TextField()
    number = models.CharField(max_length = 140)
    emailaddress = models.EmailField(max_length=254)

    def __str__(self):
        return self.title

class Parks(models.Model):
    title = models.CharField(max_length = 140)
    address = models.TextField()
    number = models.CharField(max_length = 140)
    emailaddress = models.EmailField(max_length=254)

    def __str__(self):
        return self.title

class Zoos(models.Model):
    title = models.CharField(max_length = 140)
    address = models.TextField()
    number = models.CharField(max_length = 140)
    emailaddress = models.EmailField(max_length=254)

    def __str__(self):
        return self.title

class Museums(models.Model):
    title = models.CharField(max_length = 140)
    address = models.TextField()
    number = models.CharField(max_length = 140)
    emailaddress = models.EmailField(max_length=254)

    def __str__(self):
        return self.title

class Restaurants(models.Model):
    title = models.CharField(max_length = 140)
    address = models.TextField()
    number = models.CharField(max_length = 140)
    emailaddress = models.EmailField(max_length=254)

    def __str__(self):
        return self.title

class Malls(models.Model):
    title = models.CharField(max_length = 140)
    address = models.TextField()
    number = models.CharField(max_length = 140)
    emailaddress = models.EmailField(max_length=254)

    def __str__(self):
        return self.title

class maps(models.Model):
    title = models.CharField(max_length = 140)
    image = models.ImageField(null = True,  blank = True,
                              width_field = "width_field", height_field="height_field")
    height_field = models.IntegerField(default = 0)
    width_field = models.IntegerField(default = 0)
    
    def __str__(self):
        return self.title
    


    
