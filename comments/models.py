from django.db import models


class Comment(models.Model):
    video = models.CharField(max_length=50)
    body = models.TextField(max_length=750)
    comment_likes = models.IntegerField(default=0)
    comment_dislikes = models.IntegerField(default=0)
    reply = models.TextField(max_length=750)

    def __str__(self):
        return self.Comments.title


