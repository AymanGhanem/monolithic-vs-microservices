from django.db import models

class Review(models.Model):
    reviewer        = models.CharField(max_length= 255, null= True, blank= True, default= "Default reviewer")
    movie           = models.PositiveIntegerField()
    content         = models.TextField(null= True, blank= True, default= "Default content")


    def __str__(self):
        return str(self.id)

# No Movie Model!
