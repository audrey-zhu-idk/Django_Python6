from django.db import models

# Create your models here.
class PostProject(models.Model):
    title = models.TextField()
    descr_one = models.TextField(null=True, blank=True)
    #descr_two = models.TextField(null=True, blank=True)