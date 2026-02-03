from rest_framework import serializers
from .models import Post, Comment

class RecursiveSerializer(serializers.Serializer):
    def to_representation(self, value):
        serializer = CommentSerializer(value, context=self.context)
        return serializer.data

class CommentSerializer(serializers.ModelSerializer):
    replies = RecursiveSerializer(many=True)

    class Meta:
        model = Comment
        fields = ['id', 'author', 'content', 'created_at', 'replies']

class PostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True)

    class Meta:
        model = Post
        fields = ['id', 'author', 'content', 'created_at', 'comments']
