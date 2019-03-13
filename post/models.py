from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Post(models.Model):
    user = models.ForeignKey(to=User, null=True, on_delete=models.SET_NULL)
    title = models.TextField()
    body = models.TextField()
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{str(self.user).capitalize()} {self.title}'


class Subscribe(models.Model):
    follower = models.ForeignKey(to=User, related_name='follower', null=True, on_delete=models.SET_NULL)
    following = models.ForeignKey(to=User, related_name='following', null=True, on_delete=models.SET_NULL)
