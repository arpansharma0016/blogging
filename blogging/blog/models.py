from django.db import models

class Post(models.Model):
    visitors = models.IntegerField(default=0)
    title = models.TextField()
    post = models.TextField()
    post_json = models.TextField()
    thumbnail = models.TextField()
    caption = models.TextField()
    created = models.DateField(auto_now_add=True)
