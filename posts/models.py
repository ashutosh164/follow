from django.db import models
from profiles.models import Profile


class Post(models.Model):
    author = models.ForeignKey(Profile,on_delete=models.CASCADE)
    body = models.TextField()
    update = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.body)[:30]

    class Meta:
        ordering = ('-created',)
        