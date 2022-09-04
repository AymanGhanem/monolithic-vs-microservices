from django.db import models

class Movie(models.Model):
    title           = models.CharField(max_length= 255, null= True, blank= True, default= "Defualt value")
    description     = models.TextField(null= True, blank= True, default= "Default description")

    def __str__(self):
        return str(self.id) + self.title

class Review(models.Model):
    reviewer        = models.CharField(max_length= 255, null= True, blank= True, default= "Default reviewer")
    movie           = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name= 'reviews')
    content         = models.TextField(null= True, blank= True, default= "Default content")


    def __str__(self):
        return str(self.id)