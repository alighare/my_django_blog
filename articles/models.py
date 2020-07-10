from django.db import models
from django.contrib.auth.models import User

class Articles(models.Model):
    title=models.CharField(max_length=100)
    date=models.DateTimeField(auto_now_add=True)
    body=models.TextField()
    slug=models.SlugField()
    # author
    author=models.ForeignKey(User,default=None,on_delete=models.CASCADE)
    # thumbnail
    image=models.ImageField(default="default.jpg", blank=True)
    def __str__(self):
        return self.title
    def snippet(self):
        return self.body[:50] + " ..."
