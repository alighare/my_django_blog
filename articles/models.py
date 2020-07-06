from django.db import models

class Articles(models.Model):
    title=models.CharField(max_length=100)
    date=models.DateTimeField(auto_now_add=True)
    body=models.TextField()
    slug=models.SlugField()
    # author
    # thumbnail
    def __str__(self):
        return self.title
    def snippet(self):
        return self.body[:50] + " ..."
