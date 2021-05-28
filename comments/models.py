from django.db import models


class Comment(models.Model):
    video_id = models.CharField(max_length=50)
    body = models.TextField(max_length=750)
    comment_likes = models.IntegerField(default=0)
    comment_dislikes = models.IntegerField(default=0)

    def __int__(self):
        return self.video_id


class Reply(models.Model):
    comment = models.ForeignKey('Comment')
    body = models.TextField(max_length=750)
    comment_likes = models.IntegerField(default=0)
    comment_dislikes = models.IntegerField(default=0)


