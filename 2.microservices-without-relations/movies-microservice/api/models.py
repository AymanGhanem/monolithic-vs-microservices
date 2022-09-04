from django.db import models

class Movie(models.Model):
    title           = models.CharField(max_length= 255, null= True, blank= True, default= "Defualt value")
    description     = models.TextField(null= True, blank= True, default= "Default description")

    def __str__(self):
        return str(self.id) + self.title
