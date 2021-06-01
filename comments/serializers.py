from rest_framework import serializers
from .models import Comment
from .models import Reply


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['video_id', 'body', 'comment_likes', 'comment_dislikes']


class ReplySerializer(serializers.ModelSerializer):
    class Meta:
        model = Reply
        fields = ['body', 'comment_likes', 'comment_dislikes']