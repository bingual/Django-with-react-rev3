from rest_framework import serializers
from django.contrib.auth import get_user_model

from instagram.models import Post


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = [
            'username',
            'email',
        ]


class PostSerializer(serializers.ModelSerializer):
    username = serializers.ReadOnlyField(source='author.username')    # 방법1
    # author = AuthorSerializer()   # 방법2

    class Meta:
        model = Post
        fields = [
            'pk',
            # 'author',
            'username',
            'message',
            'created_at',
            'updated_at',
            'is_public',
            'ip',
        ]
