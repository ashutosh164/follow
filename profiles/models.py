from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    following = models.ManyToManyField(User,related_name='following', blank=True)
    bio = models.TextField(default='No bio...')
    update = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def profile_post(self):
        return self.post_set.all()  # reverse relationship fetch the post data we can return by calling related name

    @property
    def follower_count(self):
        return self.following.all().count()

    def __str__(self):
        return str(self.user.username)

    class Meta:
        ordering = ('-created',)


