from django.db import models

class Blogpost(models.Model):
        title= models.TextField()
        context = models.TextField(null =True, blank= True)

