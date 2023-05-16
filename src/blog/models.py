from django.db import models

# Create your models here.
class BlogPost(models.Model):
    title = models.TextField()# default value is False
    content = models.TextField(null=True, blank=True)

# Same thing as the above, basically
# class BlogPost:
#     title = "My Title"
#     content = "Coll Content"

class Comment(models.Model):
    comment = models.TextField()