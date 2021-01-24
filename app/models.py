from django.contrib.auth.models import User
from django.db import models


class Post(models.Model):
    user_fk = models.ForeignKey(to=User, on_delete=models.CASCADE, verbose_name='Username')
    title = models.CharField(max_length=255)
    post_text = models.TextField(max_length=500)
    votes = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.user_fk.username} - {self.title}"


class Comment(models.Model):
    post_fk = models.ForeignKey(to=Post, on_delete=models.CASCADE)
    user_fk = models.ForeignKey(to=User, on_delete=models.CASCADE)
    comment_text = models.TextField(max_length=500)
    votes = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.user_fk.username} - {self.comment_text[:50]}..." \
            if len(self.comment_text) > 50 else f"{self.user_fk.username} - {self.comment_text}"

