from rest_framework import serializers

from tweet.models import Tweet, Comment


class TweetSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    last_update = serializers.IntegerField(read_only=True)


class Meta:
    model = Tweet
    field = ['id', 'text', 'last_update']


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'comment', 'tweet', 'comment_on', 'tweet']

    # id = serializers.IntegerField()
    # text = serializers.CharField(max_length=200)
    # last_updated = serializers.DateTimeField()
